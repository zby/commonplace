from __future__ import annotations

from hashlib import sha256
from pathlib import Path

import pytest

from commonplace.lib import agentic_set
from commonplace.lib.note_parser import parse_document

OVERVIEW_BODY = """# Overview

## Source register

| SRC-1 | git | `x` |

## Reconciliation

Prose mentioning MEM-OBJ-9 without mapping it.

| specialist proposal | canonical record | disposition |
|---|---|---|
| `MEM-OBJ-1` | **OBJ-2** | registered |
| MEM-RTE-1 | RTE-3 | merged into the coordinator's route |
| MEM-CLM-1 | rejected | not a claim within the boundary |

## Bounded synthesis
"""

LOCAL_REPORT = """---
type: types/agent-memory-analysis-report.md
finalized-from: null
memory-comparison:
  axes:
    storage_substrate:
      records: [MEM-OBJ-1]
---

# Report

## Shared records

### Operative objects

#### MEM-OBJ-1 — Store

Declared here; see MEM-RTE-1 and MEM-OBJ-10.

#### RTE-1 — Seeded route

Re-declared seed.

#### On OBJ-1 — Seeded object

Already an annotation.

### Routes

#### MEM-RTE-1 — Import

## Write side

### RTE-1 — Not under Shared records

Headings outside Shared records are not declarations.
"""


def test_mapping_table_reads_only_rows_with_a_proposal_and_a_canonical_id() -> None:
    assert agentic_set.proposal_mapping(OVERVIEW_BODY) == {
        "MEM-OBJ-1": "OBJ-2",
        "MEM-RTE-1": "RTE-3",
    }


def test_mapping_table_rejects_a_proposal_mapped_twice() -> None:
    body = OVERVIEW_BODY.replace("| MEM-RTE-1 | RTE-3 |", "| MEM-OBJ-1 | RTE-3 |")
    with pytest.raises(ValueError, match="MEM-OBJ-1 mapped twice"):
        agentic_set.proposal_mapping(body)


def test_finalization_maps_exact_tokens_and_annotates_re_declared_seeds() -> None:
    mapping = agentic_set.proposal_mapping(OVERVIEW_BODY)

    finalized = agentic_set.finalize_local_report(LOCAL_REPORT, mapping)

    assert "records: [OBJ-2]" in finalized
    assert "#### OBJ-2 — Store" in finalized
    assert "see RTE-3 and MEM-OBJ-10." in finalized  # MEM-OBJ-10 is not MEM-OBJ-1
    assert "#### On RTE-1 — Seeded route" in finalized
    assert finalized.count("#### On OBJ-1 — Seeded object") == 1
    assert "#### RTE-3 — Import" in finalized
    assert "### RTE-1 — Not under Shared records" in finalized


def member_from(text: str, *, amendments: str = "\n## Amendments\n\nnone\n") -> agentic_set.SetDocument:
    content = (text.rstrip("\n") + "\n" + amendments).encode("utf-8")
    document, error = parse_document(content.decode("utf-8"))
    assert error is None and document is not None
    return agentic_set.SetDocument("memory.md", Path("memory.md"), content, document)


def test_finalization_check_accepts_the_derived_member_up_to_whitespace() -> None:
    mapping = agentic_set.proposal_mapping(OVERVIEW_BODY)
    derived = agentic_set.finalize_local_report(LOCAL_REPORT, mapping)
    derived = derived.replace("finalized-from: null", f"finalized-from: {'a' * 64}")
    reflowed = derived.replace("Declared here; see", "Declared here;\nsee")

    assert agentic_set.finalization_errors(
        local_text=LOCAL_REPORT, member=member_from(reflowed), mapping=mapping
    ) == []


@pytest.mark.parametrize(
    ("edit", "expected"),
    [
        (lambda text: text.replace("Re-declared seed.", "Re-declared seed, reworded."), "body differs"),
        (lambda text: text.replace("records: [OBJ-2]", "records: [OBJ-2, RTE-3]"), "frontmatter differs"),
        (lambda text: text.replace("#### On RTE-1", "#### RTE-1"), "body differs"),
    ],
)
def test_finalization_check_rejects_content_beyond_the_derivation(edit, expected) -> None:
    mapping = agentic_set.proposal_mapping(OVERVIEW_BODY)
    derived = agentic_set.finalize_local_report(LOCAL_REPORT, mapping)

    errors = agentic_set.finalization_errors(
        local_text=LOCAL_REPORT, member=member_from(edit(derived)), mapping=mapping
    )

    assert any(expected in error for error in errors)


def test_finalization_check_requires_the_amendments_section() -> None:
    mapping = agentic_set.proposal_mapping(OVERVIEW_BODY)
    derived = agentic_set.finalize_local_report(LOCAL_REPORT, mapping)

    errors = agentic_set.finalization_errors(
        local_text=LOCAL_REPORT, member=member_from(derived, amendments=""), mapping=mapping
    )

    assert errors == ["finalization: memory member lacks its ## Amendments section"]


def write_set(root: Path, *, disposition: str = "complete") -> Path:
    members = {
        "runtime.md": "types/agentic-system-runtime-report.md",
        "memory.md": "types/agent-memory-analysis-report.md",
        "epistemic.md": "types/agentic-system-epistemic-report.md",
    }
    hashes = {}
    for name, member_type in members.items():
        run_field = "analysis-run" if name == "memory.md" else "run-id"
        content = f"---\ntype: {member_type}\n{run_field}: AAS-2026-09-28-x-01\n---\n# {name}\n".encode()
        (root / name).write_bytes(content)
        hashes[name] = sha256(content).hexdigest()
    manifest = "".join(
        f"  - path: {name}\n    sha256: {hashes[name]}\n    type: {member_type}\n"
        for name, member_type in members.items()
    )
    overview = root / "overview.md"
    overview.write_text(
        "---\ntype: types/agentic-system-analysis-overview.md\n"
        f"result-disposition: {disposition}\nrun-id: AAS-2026-09-28-x-01\n"
        + ("members:\n" + manifest if disposition == "complete" else "members: []\n")
        + "---\n# Overview\n"
    )
    return overview


def test_load_member_set_opens_every_pinned_member(tmp_path: Path) -> None:
    overview = write_set(tmp_path)

    member_set = agentic_set.load_member_set(overview)

    assert sorted(member_set.members) == ["epistemic.md", "memory.md", "runtime.md"]
    assert member_set.memory is not None
    assert member_set.documents[0].name == "overview.md"
    assert agentic_set.set_identity_errors(member_set) == []


def test_blocked_overview_loads_without_members(tmp_path: Path) -> None:
    overview = write_set(tmp_path, disposition="blocked")
    assert agentic_set.load_member_set(overview).members == {}


@pytest.mark.parametrize(
    ("edit", "expected"),
    [
        (lambda o: o.write_text(o.read_text().replace("  - path: epistemic.md", "  - path: extra.md")), "names exactly"),
        (lambda o: o.write_text(o.read_text().replace("    type: types/agentic-system-epistemic-report.md", "    type: types/agentic-system-runtime-report.md")), "must have type"),
        (lambda o: (o.parent / "runtime.md").write_bytes(b"drift"), "runtime.md bytes hash to"),
        (lambda o: (o.parent / "runtime.md").unlink(), "cannot read runtime.md"),
        (lambda o: o.write_text(o.read_text().replace("result-disposition: complete", "result-disposition: blocked")), "names no members"),
        (lambda o: o.write_text("\n".join(line for line in o.read_text().splitlines() if "epistemic" not in line) + "\n"), "names exactly"),
    ],
)
def test_load_member_set_rejects_a_broken_manifest(tmp_path: Path, edit, expected) -> None:
    overview = write_set(tmp_path)
    edit(overview)
    with pytest.raises(ValueError, match=expected):
        agentic_set.load_member_set(overview)


def test_identity_errors_are_reported_per_member() -> None:
    def document(name: str, values: str) -> agentic_set.SetDocument:
        content = f"---\n{values}\n---\n# {name}\n".encode()
        parsed, error = parse_document(content.decode())
        assert error is None and parsed is not None
        return agentic_set.SetDocument(name, Path(name), content, parsed)

    member_set = agentic_set.MemberSet(
        overview=document("overview.md", "run-id: R\nreviewed-boundary: B"),
        members={
            "runtime.md": document("runtime.md", "run-id: R\nreviewed-boundary: other"),
            "memory.md": document("memory.md", "analysis-run: R\nreviewed-boundary: B\nsource-identity: s"),
            "epistemic.md": document("epistemic.md", "run-id: other\nreviewed-boundary: B"),
        },
    )

    assert agentic_set.set_identity_errors(member_set) == [
        "runtime.md: reviewed-boundary does not match the overview",
        "epistemic.md: run-id does not match the overview",
    ]
