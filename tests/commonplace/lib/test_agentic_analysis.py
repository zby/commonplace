from __future__ import annotations

import json
import shutil
from hashlib import sha256
from pathlib import Path

import yaml

from commonplace.lib import validation

REPO_ROOT = Path(__file__).resolve().parents[3]
RUN_ID = "AAS-2026-09-03-example-system-01"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def lens_artifact(
    *,
    lens: str,
    packet_id: str,
    runtime_sha256: str,
    body: str,
    canonical_register: str = "CANON-v1-0123456789abcdef",
) -> str:
    header = {
        "run-id": RUN_ID,
        "lens": lens,
        "packet-id": packet_id,
        "reviewed-boundary": "0123456789abcdef",
        "source-register": "SRCREG-v1-0123456789abcdef",
        "canonical-register": canonical_register,
        "runtime-baseline-sha256": runtime_sha256,
    }
    return "---\n" + yaml.safe_dump(header, sort_keys=False) + "---\n\n" + body


def configure_types(tmp_path: Path) -> None:
    shutil.copytree(REPO_ROOT / "kb/types", tmp_path / "kb/types")
    report_types = tmp_path / "kb/reports/types"
    report_types.mkdir(parents=True)
    for name in (
        "agentic-system-analysis-run-state.md",
        "agentic-system-analysis-run-state.schema.yaml",
    ):
        shutil.copyfile(REPO_ROOT / "kb/reports/types" / name, report_types / name)
    write(tmp_path / "kb/reports/COLLECTION.md", "# Reports\n")


def valid_run_state(tmp_path: Path) -> Path:
    configure_types(tmp_path)
    run_dir = tmp_path / "kb/reports/state/agentic-system-analysis" / RUN_ID
    retained = tmp_path / "kb/reports/retained/agentic-analysis" / f"{RUN_ID}.md"
    result_content = f"""---
type: kb/types/agentic-system-analysis-result.md
run-id: {RUN_ID}
---

# Result
"""
    write(retained, result_content)

    runtime = write(run_dir / "runtime-baseline.md", "# Sealed runtime baseline\n")
    runtime_sha256 = digest(runtime)
    memory_packet_id = f"{RUN_ID}-MEM-P1"
    epistemic_packet_id = f"{RUN_ID}-EPI-P1"
    memory_packet = write(
        run_dir / "packets/memory-p1.md",
        lens_artifact(
            lens="memory/context",
            packet_id=memory_packet_id,
            runtime_sha256=runtime_sha256,
            body="memory packet\n",
        ),
    )
    epistemic_packet = write(
        run_dir / "packets/epistemic-p1.md",
        lens_artifact(
            lens="epistemic",
            packet_id=epistemic_packet_id,
            runtime_sha256=runtime_sha256,
            body="epistemic packet\n",
        ),
    )
    memory_return = write(
        run_dir / "returns/memory-p1.md",
        lens_artifact(
            lens="memory/context",
            packet_id=memory_packet_id,
            runtime_sha256=runtime_sha256,
            body="memory return\n",
        ),
    )
    epistemic_return = write(
        run_dir / "returns/epistemic-p1.md",
        lens_artifact(
            lens="epistemic",
            packet_id=epistemic_packet_id,
            runtime_sha256=runtime_sha256,
            body="epistemic return\n",
        ),
    )

    canonical_entry = retained.relative_to(tmp_path).as_posix()
    receipt_payload = {
        "schema": "commonplace.validation.v1",
        "status": "success",
        "summary": {"files_analysed": 1},
        "analysed_artifacts": [
            {
                "path": canonical_entry,
                "type": "agentic-system-analysis-result",
                "warnings": 0,
                "failures": 0,
            }
        ],
    }
    receipt = write(
        run_dir / "validation.json",
        json.dumps(receipt_payload, sort_keys=True) + "\n",
    )

    result_sha256 = digest(retained)
    source_root = tmp_path / "frozen-source"
    source_root.mkdir()
    frontmatter = {
        "type": "kb/reports/types/agentic-system-analysis-run-state.md",
        "description": f"Operational state for {RUN_ID} through handoff readiness",
        "run-id": RUN_ID,
        "phase": "handoff-ready",
        "producer": "kb/instructions/analyse-agentic-system/SKILL.md",
        "canonical-carrier": "retained",
        "canonical-physical-form": "one file",
        "canonical-entry": canonical_entry,
        "canonical-manifest": None,
        "canonical-consumers": ["operator handoff", "acceptance audit"],
        "retention-rule": "Keep while the acceptance audit consumes exact bytes.",
        "cleanup-condition": "The retained audit is explicitly retired.",
        "permitted-projections": ["kb/agentic-systems/example-system.md"],
        "write-authority": [
            f"kb/reports/state/agentic-system-analysis/{RUN_ID}/",
            "kb/reports/retained/agentic-analysis/",
        ],
        "source-kind": "checkout",
        "source-revision": "0123456789abcdef",
        "source-capture": "checkout at 0123456789abcdef",
        "source-capture-path": source_root.as_posix(),
        "source-byte-length": None,
        "source-sha256": None,
        "source-root": source_root.as_posix(),
        "source-register": "SRCREG-v1-0123456789abcdef",
        "canonical-register": "CANON-v1-0123456789abcdef",
        "runtime-baseline-path": "runtime-baseline.md",
        "runtime-baseline-sha256": runtime_sha256,
        "lens-packets": [
            {
                "id": memory_packet_id,
                "lens": "memory/context",
                "path": "packets/memory-p1.md",
                "sha256": digest(memory_packet),
                "source-register": "SRCREG-v1-0123456789abcdef",
                "canonical-register": "CANON-v1-0123456789abcdef",
                "runtime-baseline-sha256": runtime_sha256,
            },
            {
                "id": epistemic_packet_id,
                "lens": "epistemic",
                "path": "packets/epistemic-p1.md",
                "sha256": digest(epistemic_packet),
                "source-register": "SRCREG-v1-0123456789abcdef",
                "canonical-register": "CANON-v1-0123456789abcdef",
                "runtime-baseline-sha256": runtime_sha256,
            },
        ],
        "lens-returns": [
            {
                "packet-id": memory_packet_id,
                "path": "returns/memory-p1.md",
                "sha256": digest(memory_return),
            },
            {
                "packet-id": epistemic_packet_id,
                "path": "returns/epistemic-p1.md",
                "sha256": digest(epistemic_return),
            },
        ],
        "accepted-lens-packets": [memory_packet_id, epistemic_packet_id],
        "corrections": [],
        "reconciliation-seal": sha256(b"reconciled").hexdigest(),
        "assembled-entry": canonical_entry,
        "assembled-entry-byte-length": len(retained.read_bytes()),
        "assembled-entry-sha256": result_sha256,
        "assembled-manifest": None,
        "assembled-manifest-byte-length": None,
        "assembled-manifest-sha256": None,
        "validation-target": canonical_entry,
        "validation-target-sha256": result_sha256,
        "validation-receipt-path": "validation.json",
        "validation-receipt-sha256": digest(receipt),
        "handoff-entry-sha256": result_sha256,
        "handoff-manifest-sha256": None,
    }
    body = f"""# Agentic-system analysis run state — {RUN_ID}

## Authority and lifecycle

Declared before source inspection.

## Source and phase receipts

Reached handoff readiness in order.

## Packet and correction ledger

Both lens returns were accepted.

## Diagnostics and handoff

No execution failures.
"""
    state = run_dir / "run-state.md"
    return write(
        state,
        "---\n" + yaml.safe_dump(frontmatter, sort_keys=False) + "---\n\n" + body,
    )


def test_handoff_ready_run_state_verifies_all_owned_bytes(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.note_type == "agentic-system-analysis-run-state"
    assert results.fails == []
    assert any("handoff entry: type and run-id match" in item for item in results.passes)
    assert any("one intended agentic-system-analysis-result" in item for item in results.passes)


def test_run_state_fails_after_canonical_result_bytes_change(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    result = next((tmp_path / "kb/reports/retained").rglob(f"{RUN_ID}.md"))
    result.write_text(result.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("assembled entry: SHA-256 mismatch" in item for item in results.fails)


def test_run_state_rejects_an_invalidated_accepted_packet(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    frontmatter = document.frontmatter
    first_packet = frontmatter["accepted-lens-packets"][0]
    replacement = f"{RUN_ID}-MEM-P2"
    replacement_register = "CANON-v2-0123456789abcdef"
    replacement_packet = write(
        state.parent / "packets/memory-p2.md",
        lens_artifact(
            lens="memory/context",
            packet_id=replacement,
            runtime_sha256=frontmatter["runtime-baseline-sha256"],
            canonical_register=replacement_register,
            body="replacement memory packet\n",
        ),
    )
    replacement_return = write(
        state.parent / "returns/memory-p2.md",
        lens_artifact(
            lens="memory/context",
            packet_id=replacement,
            runtime_sha256=frontmatter["runtime-baseline-sha256"],
            canonical_register=replacement_register,
            body="replacement memory return\n",
        ),
    )
    frontmatter["lens-packets"].append(
        {
            "id": replacement,
            "lens": "memory/context",
            "path": "packets/memory-p2.md",
            "sha256": digest(replacement_packet),
            "source-register": frontmatter["source-register"],
            "canonical-register": replacement_register,
            "runtime-baseline-sha256": frontmatter["runtime-baseline-sha256"],
        }
    )
    frontmatter["lens-returns"].append(
        {
            "packet-id": replacement,
            "path": "returns/memory-p2.md",
            "sha256": digest(replacement_return),
        }
    )
    frontmatter["canonical-register"] = replacement_register
    frontmatter["corrections"] = [
        {
            "id": f"{RUN_ID}-CORR-1",
            "invalidated-packets": [first_packet],
            "replacement-packets": [replacement],
            "from-canonical-register": "CANON-v1-0123456789abcdef",
            "to-canonical-register": replacement_register,
            "reason": "Same-boundary evidence corrected one record.",
        }
    ]
    state.write_text(
        "---\n"
        + yaml.safe_dump(frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("invalidated packets cannot be accepted" in item for item in results.fails)


def test_run_state_rejects_a_receipt_for_the_wrong_type(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    run_dir = state.parent
    receipt = run_dir / "validation.json"
    payload = json.loads(receipt.read_text(encoding="utf-8"))
    payload["analysed_artifacts"][0]["type"] = "text"
    receipt.write_text(json.dumps(payload, sort_keys=True) + "\n", encoding="utf-8")

    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    document.frontmatter["validation-receipt-sha256"] = digest(receipt)
    state.write_text(
        "---\n"
        + yaml.safe_dump(document.frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("expected one successful" in item for item in results.fails)


def test_run_state_rejects_a_return_with_a_mismatched_packet_header(
    tmp_path: Path,
) -> None:
    state = valid_run_state(tmp_path)
    returned = state.parent / "returns/memory-p1.md"
    returned.write_text(
        returned.read_text(encoding="utf-8").replace(
            f"packet-id: {RUN_ID}-MEM-P1",
            f"packet-id: {RUN_ID}-MEM-P2",
        ),
        encoding="utf-8",
    )

    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    document.frontmatter["lens-returns"][0]["sha256"] = digest(returned)
    state.write_text(
        "---\n"
        + yaml.safe_dump(document.frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("packet header does not match" in item for item in results.fails)


def test_run_state_verifies_repository_archive_identity(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    archive = write(tmp_path / "capture.tar.gz", "frozen archive bytes\n")
    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    document.frontmatter.update(
        {
            "source-kind": "repository-archive",
            "source-capture": "commit-pinned archive",
            "source-capture-path": archive.as_posix(),
            "source-byte-length": len(archive.read_bytes()),
            "source-sha256": digest(archive),
        }
    )
    state.write_text(
        "---\n"
        + yaml.safe_dump(document.frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []
    assert any("source archive: byte identity matches" in item for item in results.passes)


def test_reconciliation_may_advance_the_register_from_accepted_proposals(
    tmp_path: Path,
) -> None:
    state = valid_run_state(tmp_path)
    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    document.frontmatter["canonical-register"] = "CANON-v2-accepted-proposals"
    state.write_text(
        "---\n"
        + yaml.safe_dump(document.frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []
