from __future__ import annotations

from hashlib import sha256
from pathlib import Path

import pytest

from commonplace.lib import agentic_set
from commonplace.lib.note_parser import parse_document


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

    assert agentic_set.set_identity_errors(member_set, source_identity="t") == [
        "runtime.md: reviewed-boundary does not match the overview",
        "memory.md: source-identity does not match the frozen source",
        "epistemic.md: run-id does not match the overview",
    ]
