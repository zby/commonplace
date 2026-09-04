from __future__ import annotations

import json
import shutil
import subprocess
from hashlib import sha256
from pathlib import Path

import yaml

from commonplace.cli import agentic_analysis_handoff
from commonplace.lib import validation
from commonplace.lib.agentic_analysis import (
    parse_agentic_analysis_run_state,
    render_agentic_analysis_handoff,
)

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
    reviewed_boundary: str = "0123456789abcdef",
    canonical_register: str = "CANON-v1-0123456789abcdef",
) -> str:
    header = {
        "run-id": RUN_ID,
        "lens": lens,
        "packet-id": packet_id,
        "reviewed-boundary": reviewed_boundary,
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


def valid_run_state(tmp_path: Path) -> Path:
    configure_types(tmp_path)
    run_dir = tmp_path / "kb/reports/state/agentic-system-analysis" / RUN_ID
    source_root, source_revision = git_checkout(
        tmp_path / "related-systems/example--system"
    )
    retained = tmp_path / "kb/reports/retained/agentic-analysis" / f"{RUN_ID}.md"
    result_content = f"""---
type: kb/types/agentic-system-analysis-result.md
description: Complete fixture analysis at {source_revision}
run-id: {RUN_ID}
system: Example System
run-date: '2026-09-03'
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: {source_revision}
analysis-cutoff: '2026-09-03'
evidence-tier: code-grounded
---

# Result
"""
    write(retained, result_content)

    runtime_header = {
        "run-id": RUN_ID,
        "reviewed-boundary": source_revision,
        "source-register": "SRCREG-v1-0123456789abcdef",
        "canonical-register": "CANON-v1-0123456789abcdef",
        "route-closure": [
            {
                "route-id": "RTE-1",
                "immediate-return": "Result returned to the invoking client.",
                "later-read-back": "No later read-back in this fixture.",
                "delegated-visibility": "No delegated consumer in this fixture.",
                "selection-predicate": "The single fixture route is selected.",
                "invalidation-or-expiry": "The fixture has no retained state.",
                "activation-or-effect": "The client receives the terminal result.",
                "evidence-and-limits": "Static fixture evidence only.",
            }
        ],
    }
    runtime = write(
        run_dir / "runtime-baseline.md",
        "---\n"
        + yaml.safe_dump(runtime_header, sort_keys=False)
        + "---\n\n# Sealed runtime baseline\n\n"
        + "## Canonical routes\n\n"
        + "| ID | Route |\n|---|---|\n| RTE-1 | Fixture route |\n",
    )
    runtime_sha256 = digest(runtime)
    diagnostic_ledger = write(run_dir / "diagnostics.jsonl", "")
    memory_packet_id = f"{RUN_ID}-MEM-P1"
    epistemic_packet_id = f"{RUN_ID}-EPI-P1"
    memory_packet = write(
        run_dir / "packets/memory-p1.md",
        lens_artifact(
            lens="memory/context",
            packet_id=memory_packet_id,
            runtime_sha256=runtime_sha256,
            body="memory packet\n",
            reviewed_boundary=source_revision,
        ),
    )
    epistemic_packet = write(
        run_dir / "packets/epistemic-p1.md",
        lens_artifact(
            lens="epistemic",
            packet_id=epistemic_packet_id,
            runtime_sha256=runtime_sha256,
            body="epistemic packet\n",
            reviewed_boundary=source_revision,
        ),
    )
    memory_return = write(
        run_dir / "returns/memory-p1.md",
        lens_artifact(
            lens="memory/context",
            packet_id=memory_packet_id,
            runtime_sha256=runtime_sha256,
            body="memory return\n",
            reviewed_boundary=source_revision,
        ),
    )
    epistemic_return = write(
        run_dir / "returns/epistemic-p1.md",
        lens_artifact(
            lens="epistemic",
            packet_id=epistemic_packet_id,
            runtime_sha256=runtime_sha256,
            body="epistemic return\n",
            reviewed_boundary=source_revision,
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
        "source-revision": source_revision,
        "source-capture": f"checkout containing commit {source_revision}",
        "source-capture-path": source_root.as_posix(),
        "source-byte-length": None,
        "source-sha256": None,
        "source-root": source_root.as_posix(),
        "source-register": "SRCREG-v1-0123456789abcdef",
        "canonical-register": "CANON-v1-0123456789abcdef",
        "runtime-baseline-path": "runtime-baseline.md",
        "runtime-baseline-sha256": runtime_sha256,
        "runtime-baseline-canonical-register": "CANON-v1-0123456789abcdef",
        "diagnostic-ledger-path": "diagnostics.jsonl",
        "diagnostic-ledger-byte-length": 0,
        "diagnostic-ledger-sha256": digest(diagnostic_ledger),
        "lens-return-byte-budget": 32768,
        "lens-packets": [
            {
                "id": memory_packet_id,
                "lens": "memory/context",
                "path": "packets/memory-p1.md",
                "sha256": digest(memory_packet),
                "byte-length": len(memory_packet.read_bytes()),
                "source-register": "SRCREG-v1-0123456789abcdef",
                "canonical-register": "CANON-v1-0123456789abcdef",
                "runtime-baseline-sha256": runtime_sha256,
            },
            {
                "id": epistemic_packet_id,
                "lens": "epistemic",
                "path": "packets/epistemic-p1.md",
                "sha256": digest(epistemic_packet),
                "byte-length": len(epistemic_packet.read_bytes()),
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
                "byte-length": len(memory_return.read_bytes()),
            },
            {
                "packet-id": epistemic_packet_id,
                "path": "returns/epistemic-p1.md",
                "sha256": digest(epistemic_return),
                "byte-length": len(epistemic_return.read_bytes()),
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
        "handoff": {
            "lens-runs": [
                {
                    "lens": "memory/context",
                    "scope": "RTE-1 and its fixture result",
                    "depth": "brief",
                },
                {
                    "lens": "epistemic",
                    "scope": "RTE-1 and its fixture result",
                    "depth": "brief",
                },
            ],
            "legacy-memory-review": {
                "detection": "not-detected",
                "invocation": "not-applicable",
                "location": None,
                "validation": "Not applicable to this fixture.",
            },
            "transfer-scan": {
                "disposition": "not-requested",
                "location": None,
            },
            "retention-disposition": "Retain through the fixture acceptance audit.",
            "limitations": ["Static fixture evidence only."],
            "blockers": [],
        },
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
    assert any(
        "source checkout: recorded commit resolves independently of HEAD" in item
        for item in results.passes
    )
    assert any("handoff entry: type and run-id match" in item for item in results.passes)
    assert any("one intended agentic-system-analysis-result" in item for item in results.passes)


def test_checkout_head_may_move_after_source_revision_is_recorded(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    source_root = Path(document.frontmatter["source-root"])
    recorded_revision = document.frontmatter["source-revision"]

    write(source_root / "later.md", "later checkout state\n")
    subprocess.run(["git", "-C", str(source_root), "add", "later.md"], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(source_root),
            "-c",
            "user.name=Commonplace Test",
            "-c",
            "user.email=test@example.invalid",
            "commit",
            "--quiet",
            "-m",
            "Move checkout head",
        ],
        check=True,
    )

    assert subprocess.run(
        ["git", "-C", str(source_root), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip() != recorded_revision
    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []
    assert any(
        f"independently of HEAD at {recorded_revision}" in item
        for item in results.passes
    )


def test_checkout_revision_must_resolve_from_source_root(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    document.frontmatter["source-revision"] = "0" * 40
    state.write_text(
        "---\n"
        + yaml.safe_dump(document.frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any(
        "source checkout: recorded commit does not resolve" in item
        for item in results.fails
    )


def test_checkout_capture_path_must_equal_source_root(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    document.frontmatter["source-capture-path"] = tmp_path.as_posix()
    state.write_text(
        "---\n"
        + yaml.safe_dump(document.frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("expected the same path as source-root" in item for item in results.fails)


def test_runtime_artifact_paths_must_be_run_relative(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    document.frontmatter["runtime-baseline-path"] = (
        state.parent / "runtime-baseline.md"
    ).as_posix()
    state.write_text(
        "---\n"
        + yaml.safe_dump(document.frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("expected a normalized run-relative path" in item for item in results.fails)


def test_file_result_paths_must_be_repository_relative_kb_paths(
    tmp_path: Path,
) -> None:
    state = valid_run_state(tmp_path)
    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    document.frontmatter["assembled-entry"] = "result.md"
    state.write_text(
        "---\n"
        + yaml.safe_dump(document.frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any(
        "expected a normalized repository-relative kb/ path" in item
        for item in results.fails
    )


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
            "byte-length": len(replacement_packet.read_bytes()),
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
            "byte-length": len(replacement_return.read_bytes()),
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


def test_runtime_baseline_requires_route_closure_for_every_canonical_route(
    tmp_path: Path,
) -> None:
    state = valid_run_state(tmp_path)
    runtime = state.parent / "runtime-baseline.md"
    content = runtime.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    document.frontmatter["route-closure"] = []
    runtime.write_text(
        "---\n"
        + yaml.safe_dump(document.frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )

    state_content = state.read_text(encoding="utf-8")
    state_document, error = validation.parse_document(state_content)
    assert (
        error is None
        and state_document is not None
        and state_document.frontmatter is not None
    )
    state_document.frontmatter["runtime-baseline-sha256"] = digest(runtime)
    for packet in state_document.frontmatter["lens-packets"]:
        packet["runtime-baseline-sha256"] = digest(runtime)
    state.write_text(
        "---\n"
        + yaml.safe_dump(state_document.frontmatter, sort_keys=False)
        + "---\n"
        + state_document.body,
        encoding="utf-8",
    )

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("route-closure must be a non-empty list" in item for item in results.fails)


def test_handoff_rejects_a_basename_only_source_anchor(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    result = next((tmp_path / "kb/reports/retained").rglob(f"{RUN_ID}.md"))
    result.write_text(
        result.read_text(encoding="utf-8")
        + "\nSource evidence: SRC-1, `agent-run.ts:1`.\n",
        encoding="utf-8",
    )
    _refresh_result_identities(state, result)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("agent-run.ts: path does not resolve" in item for item in results.fails)


def test_handoff_rejects_a_source_anchor_past_the_blob_end(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    result = next((tmp_path / "kb/reports/retained").rglob(f"{RUN_ID}.md"))
    result.write_text(
        result.read_text(encoding="utf-8")
        + "\nSource evidence: SRC-1, `README.md:99`.\n",
        encoding="utf-8",
    )
    _refresh_result_identities(state, result)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("outside the recorded blob's" in item for item in results.fails)


def test_handoff_rejects_a_github_anchor_at_another_revision(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    result = next((tmp_path / "kb/reports/retained").rglob(f"{RUN_ID}.md"))
    result.write_text(
        result.read_text(encoding="utf-8")
        + "\n[Source](https://github.com/example/system/blob/"
        + "0" * 40
        + "/README.md#L1).\n",
        encoding="utf-8",
    )
    _refresh_result_identities(state, result)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("GitHub anchor uses revision" in item for item in results.fails)


def test_handoff_accepts_full_local_and_github_source_anchors(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    state_content = state.read_text(encoding="utf-8")
    state_document, error = validation.parse_document(state_content)
    assert (
        error is None
        and state_document is not None
        and state_document.frontmatter is not None
    )
    revision = state_document.frontmatter["source-revision"]
    result = next((tmp_path / "kb/reports/retained").rglob(f"{RUN_ID}.md"))
    result.write_text(
        result.read_text(encoding="utf-8")
        + "\nSource evidence: SRC-1, `README.md:1`; "
        + f"[pinned](https://github.com/example/system/blob/{revision}/README.md#L1).\n",
        encoding="utf-8",
    )
    _refresh_result_identities(state, result)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []
    assert any("README.md" in item and "resolve at" in item for item in results.passes)


def _refresh_result_identities(state: Path, result: Path) -> None:
    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    result_sha256 = digest(result)
    document.frontmatter["assembled-entry-byte-length"] = len(result.read_bytes())
    document.frontmatter["assembled-entry-sha256"] = result_sha256
    document.frontmatter["validation-target-sha256"] = result_sha256
    document.frontmatter["handoff-entry-sha256"] = result_sha256
    state.write_text(
        "---\n"
        + yaml.safe_dump(document.frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )


def _replace_diagnostics(state: Path, records: list[dict[str, object]]) -> None:
    ledger = state.parent / "diagnostics.jsonl"
    ledger.write_text(
        "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
        encoding="utf-8",
    )
    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    document.frontmatter["diagnostic-ledger-byte-length"] = len(ledger.read_bytes())
    document.frontmatter["diagnostic-ledger-sha256"] = digest(ledger)
    state.write_text(
        "---\n"
        + yaml.safe_dump(document.frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )


def test_diagnostic_ledger_accepts_a_recovered_failure(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    _replace_diagnostics(
        state,
        [
            {
                "id": f"{RUN_ID}-DIAG-001",
                "producer": "orchestrator",
                "phase": "source-frozen",
                "operation": "git show <revision>:missing.md",
                "working-directory": tmp_path.as_posix(),
                "relevant-environment": ["git test fixture"],
                "outcome": "failed",
                "classification": "execution-error",
                "exit-status": 128,
                "exact-output": "fatal: path missing.md does not exist",
                "material": True,
                "disposition": "recovered",
                "recovery": "Enumerated the tree and inspected the resolved path.",
            }
        ],
    )

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []
    assert any("1 structured record(s) verified" in item for item in results.passes)


def test_unreported_unresolved_material_diagnostic_blocks_handoff(
    tmp_path: Path,
) -> None:
    state = valid_run_state(tmp_path)
    diagnostic_id = f"{RUN_ID}-DIAG-001"
    _replace_diagnostics(
        state,
        [
            {
                "id": diagnostic_id,
                "producer": "orchestrator",
                "phase": "source-frozen",
                "operation": "source inspection that could not be recovered",
                "working-directory": tmp_path.as_posix(),
                "relevant-environment": [],
                "outcome": "truncated",
                "classification": "harness-error",
                "exit-status": 0,
                "exact-output": "partial output",
                "material": True,
                "disposition": "unresolved",
            }
        ],
    )

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any(diagnostic_id in item and "not named" in item for item in results.fails)


def test_operator_handoff_is_rendered_from_checked_state(tmp_path: Path) -> None:
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

    for label in (
        "**Result:**",
        "**System and disposition:**",
        "**Lifecycle:**",
        "**Boundary:**",
        "**Lens runs:**",
        "**Legacy memory review:**",
        "**Stable-result verification:**",
        "**Transfer scan:**",
        "**Retention disposition:**",
        "**Limitations:**",
        "**Blockers:**",
    ):
        assert label in rendered
    assert RUN_ID in rendered
    assert "memory/context: brief" in rendered


def test_lens_return_cannot_exceed_the_declared_byte_budget(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    document.frontmatter["lens-return-byte-budget"] = 1
    state.write_text(
        "---\n"
        + yaml.safe_dump(document.frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any(
        "exceeds the declared lens-return-byte-budget" in item
        for item in results.fails
    )


def test_handoff_command_refuses_an_incomplete_handoff(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    state = valid_run_state(tmp_path)
    content = state.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    document.frontmatter["handoff"] = None
    state.write_text(
        "---\n"
        + yaml.safe_dump(document.frontmatter, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)

    exit_code = agentic_analysis_handoff.main(
        [state.relative_to(tmp_path).as_posix()]
    )

    assert exit_code == 1
    assert "handoff" in capsys.readouterr().err


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
    output = capsys.readouterr().out

    assert exit_code == 0
    assert f"# Agentic-system analysis handoff — {RUN_ID}" in output
    assert "**Lifecycle:**" in output
    assert "**Blockers:** none" in output
