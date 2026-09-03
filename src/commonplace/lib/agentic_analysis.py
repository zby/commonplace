"""Parsing and integrity checks for agentic-system analysis run state."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path, PurePosixPath
from typing import Any

from commonplace.lib.note_parser import ParsedDocument, parse_document

AGENTIC_ANALYSIS_RUN_TYPE = (
    "kb/reports/types/agentic-system-analysis-run-state.md"
)
AGENTIC_ANALYSIS_RESULT_TYPE = "kb/types/agentic-system-analysis-result.md"

_PHASES = (
    "opened",
    "source-frozen",
    "runtime-sealed",
    "lenses-issued",
    "lenses-complete",
    "reconciled",
    "assembled",
    "validated",
    "handoff-ready",
)
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class FileIdentity:
    role: str
    display_path: str
    path: Path
    expected_sha256: str
    expected_bytes: int | None = None


@dataclass(frozen=True)
class LensPacket:
    packet_id: str
    lens: str
    identity: FileIdentity
    source_register: str
    canonical_register: str
    runtime_baseline_sha256: str


@dataclass(frozen=True)
class AgenticAnalysisRunState:
    path: Path
    run_dir: Path
    frontmatter: dict[str, Any]
    run_id: str
    phase: str
    carrier: str
    physical_form: str
    source_kind: str | None
    source_revision: str | None
    source_capture: FileIdentity | None
    source_root: Path | None
    source_register: str | None
    canonical_register: str | None
    canonical_entry: Path | None
    canonical_manifest: Path | None
    runtime_baseline: FileIdentity | None
    lens_packets: tuple[LensPacket, ...]
    lens_returns: tuple[tuple[str, FileIdentity], ...]
    accepted_packet_ids: tuple[str, ...]
    corrections: tuple[dict[str, Any], ...]
    assembled_entry: FileIdentity | None
    assembled_manifest: FileIdentity | None
    validation_target: str | None
    validation_target_sha256: str | None
    validation_receipt: FileIdentity | None
    handoff_entry_sha256: str | None
    handoff_manifest_sha256: str | None


def _required_string(values: dict[str, Any], field: str) -> str:
    value = values.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field}: expected a non-empty string")
    return value


def _optional_string(values: dict[str, Any], field: str) -> str | None:
    value = values.get(field)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field}: expected null or a non-empty string")
    return value


def _required_sha256(values: dict[str, Any], field: str) -> str:
    value = _required_string(values, field)
    if not _SHA256_RE.fullmatch(value):
        raise ValueError(f"{field}: expected a lowercase SHA-256 hex digest")
    return value


def _optional_sha256(values: dict[str, Any], field: str) -> str | None:
    value = _optional_string(values, field)
    if value is not None and not _SHA256_RE.fullmatch(value):
        raise ValueError(f"{field}: expected null or a lowercase SHA-256 hex digest")
    return value


def _string_list(values: dict[str, Any], field: str) -> tuple[str, ...]:
    value = values.get(field)
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item.strip() for item in value
    ):
        raise ValueError(f"{field}: expected a list of non-empty strings")
    if len(value) != len(set(value)):
        raise ValueError(f"{field}: duplicate values are not allowed")
    return tuple(value)


def _mapping_list(values: dict[str, Any], field: str) -> tuple[dict[str, Any], ...]:
    value = values.get(field)
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise ValueError(f"{field}: expected a list of mappings")
    return tuple(value)


def _state_relative_file(value: str, *, run_dir: Path, field: str) -> Path:
    pure = PurePosixPath(value)
    if pure.is_absolute() or value != pure.as_posix() or ".." in pure.parts:
        raise ValueError(f"{field}: expected a normalized run-relative path")
    if not pure.parts:
        raise ValueError(f"{field}: expected a file path")
    candidate = run_dir.joinpath(*pure.parts)
    try:
        candidate.resolve(strict=False).relative_to(run_dir.resolve())
    except ValueError as exc:
        raise ValueError(f"{field}: path escapes the run directory") from exc
    return candidate


def _repo_relative_file(value: str, *, repo_root: Path, field: str) -> Path:
    pure = PurePosixPath(value)
    if (
        pure.is_absolute()
        or value != pure.as_posix()
        or ".." in pure.parts
        or not pure.parts
        or pure.parts[0] != "kb"
    ):
        raise ValueError(f"{field}: expected a normalized repository-relative kb/ path")
    candidate = repo_root.joinpath(*pure.parts)
    try:
        candidate.resolve(strict=False).relative_to(repo_root.resolve())
    except ValueError as exc:
        raise ValueError(f"{field}: path escapes the repository") from exc
    return candidate


def _result_file(value: str, *, repo_root: Path, carrier: str, field: str) -> Path:
    candidate = Path(value)
    if candidate.is_absolute():
        if carrier != "response":
            raise ValueError(f"{field}: only a response carrier may use an absolute path")
        return candidate
    return _repo_relative_file(value, repo_root=repo_root, field=field)


def _file_identity(
    values: dict[str, Any],
    *,
    role: str,
    path_field: str,
    hash_field: str,
    run_dir: Path,
    bytes_field: str | None = None,
) -> FileIdentity | None:
    display_path = _optional_string(values, path_field)
    expected_sha256 = _optional_sha256(values, hash_field)
    if display_path is None and expected_sha256 is None:
        return None
    if display_path is None or expected_sha256 is None:
        raise ValueError(f"{role}: path and SHA-256 must be set together")
    expected_bytes: int | None = None
    if bytes_field is not None:
        raw_bytes = values.get(bytes_field)
        if not isinstance(raw_bytes, int) or isinstance(raw_bytes, bool) or raw_bytes < 0:
            raise ValueError(f"{bytes_field}: expected a non-negative integer")
        expected_bytes = raw_bytes
    return FileIdentity(
        role=role,
        display_path=display_path,
        path=_state_relative_file(display_path, run_dir=run_dir, field=path_field),
        expected_sha256=expected_sha256,
        expected_bytes=expected_bytes,
    )


def _assembled_identity(
    values: dict[str, Any],
    *,
    role: str,
    path_field: str,
    hash_field: str,
    bytes_field: str,
    repo_root: Path,
    carrier: str,
) -> FileIdentity | None:
    display_path = _optional_string(values, path_field)
    expected_sha256 = _optional_sha256(values, hash_field)
    raw_bytes = values.get(bytes_field)
    if display_path is None and expected_sha256 is None and raw_bytes is None:
        return None
    if display_path is None or expected_sha256 is None:
        raise ValueError(f"{role}: path, byte length, and SHA-256 must be set together")
    if not isinstance(raw_bytes, int) or isinstance(raw_bytes, bool) or raw_bytes < 0:
        raise ValueError(f"{bytes_field}: expected a non-negative integer")
    return FileIdentity(
        role=role,
        display_path=display_path,
        path=_result_file(
            display_path, repo_root=repo_root, carrier=carrier, field=path_field
        ),
        expected_sha256=expected_sha256,
        expected_bytes=raw_bytes,
    )


def _external_file_identity(
    values: dict[str, Any],
    *,
    role: str,
    path_field: str,
    hash_field: str,
    bytes_field: str,
) -> FileIdentity | None:
    display_path = _optional_string(values, path_field)
    expected_sha256 = _optional_sha256(values, hash_field)
    raw_bytes = values.get(bytes_field)
    if display_path is None and expected_sha256 is None and raw_bytes is None:
        return None
    if display_path is None or expected_sha256 is None:
        raise ValueError(f"{role}: path, byte length, and SHA-256 must be set together")
    if not isinstance(raw_bytes, int) or isinstance(raw_bytes, bool) or raw_bytes < 0:
        raise ValueError(f"{bytes_field}: expected a non-negative integer")
    path = Path(display_path)
    if not path.is_absolute():
        raise ValueError(f"{path_field}: expected an absolute acquisition path")
    return FileIdentity(
        role=role,
        display_path=display_path,
        path=path,
        expected_sha256=expected_sha256,
        expected_bytes=raw_bytes,
    )


def parse_agentic_analysis_run_state(
    path: Path,
    document: ParsedDocument,
    *,
    repo_root: Path,
) -> AgenticAnalysisRunState:
    """Build the guarded runtime view from an already parsed run-state record."""
    repo_root = repo_root.resolve()
    state_path = path.resolve()
    state_root = (
        repo_root / "kb" / "reports" / "state" / "agentic-system-analysis"
    ).resolve()
    try:
        relative = state_path.relative_to(state_root)
    except ValueError as exc:
        raise ValueError(
            "run-state path: expected kb/reports/state/agentic-system-analysis/"
            "<run-id>/run-state.md"
        ) from exc
    if len(relative.parts) != 2 or relative.name != "run-state.md":
        raise ValueError(
            "run-state path: expected kb/reports/state/agentic-system-analysis/"
            "<run-id>/run-state.md"
        )

    frontmatter = document.frontmatter
    if frontmatter is None:
        raise ValueError("run state: missing frontmatter")
    if frontmatter.get("type") != AGENTIC_ANALYSIS_RUN_TYPE:
        raise ValueError(f"type: expected {AGENTIC_ANALYSIS_RUN_TYPE}")

    run_id = _required_string(frontmatter, "run-id")
    if relative.parts[0] != run_id:
        raise ValueError("run-id: expected the run-state parent directory name")

    phase = _required_string(frontmatter, "phase")
    if phase not in _PHASES:
        raise ValueError(f"phase: expected one of {', '.join(_PHASES)}")
    carrier = _required_string(frontmatter, "canonical-carrier")
    if carrier not in {"response", "state", "retained"}:
        raise ValueError("canonical-carrier: expected response, state, or retained")
    physical_form = _required_string(frontmatter, "canonical-physical-form")
    if physical_form not in {"response", "one file", "package"}:
        raise ValueError(
            "canonical-physical-form: expected response, one file, or package"
        )

    canonical_entry_value = _optional_string(frontmatter, "canonical-entry")
    canonical_entry = (
        None
        if canonical_entry_value is None
        else _repo_relative_file(
            canonical_entry_value, repo_root=repo_root, field="canonical-entry"
        )
    )
    canonical_manifest_value = _optional_string(frontmatter, "canonical-manifest")
    canonical_manifest = (
        None
        if canonical_manifest_value is None
        else _repo_relative_file(
            canonical_manifest_value,
            repo_root=repo_root,
            field="canonical-manifest",
        )
    )
    if carrier == "response":
        if (
            physical_form != "response"
            or canonical_entry is not None
            or canonical_manifest is not None
        ):
            raise ValueError(
                "response carrier: requires response physical form and null canonical paths"
            )
    else:
        if physical_form == "response" or canonical_entry is None:
            raise ValueError(
                "file carrier: requires one file or package and a canonical-entry"
            )
        expected_root = repo_root / "kb" / "reports" / carrier
        try:
            canonical_entry.relative_to(expected_root.resolve())
        except ValueError as exc:
            raise ValueError(
                f"canonical-entry: expected a path under kb/reports/{carrier}/"
            ) from exc
        if physical_form == "package":
            if canonical_manifest is None:
                raise ValueError("package form: requires canonical-manifest")
            try:
                canonical_manifest.relative_to(expected_root.resolve())
            except ValueError as exc:
                raise ValueError(
                    f"canonical-manifest: expected a path under kb/reports/{carrier}/"
                ) from exc
        elif canonical_manifest is not None:
            raise ValueError("canonical-manifest: only package form uses a manifest")

    source_kind = _optional_string(frontmatter, "source-kind")
    source_revision = _optional_string(frontmatter, "source-revision")
    source_capture = None
    if source_kind == "repository-archive":
        source_capture = _external_file_identity(
            frontmatter,
            role="source archive",
            path_field="source-capture-path",
            hash_field="source-sha256",
            bytes_field="source-byte-length",
        )
    source_root_value = _optional_string(frontmatter, "source-root")
    source_root = None if source_root_value is None else Path(source_root_value)
    if source_root is not None and not source_root.is_absolute():
        raise ValueError("source-root: expected an absolute frozen source root")

    run_dir = state_path.parent
    runtime_baseline = _file_identity(
        frontmatter,
        role="runtime baseline",
        path_field="runtime-baseline-path",
        hash_field="runtime-baseline-sha256",
        run_dir=run_dir,
    )

    packets: list[LensPacket] = []
    packet_ids: set[str] = set()
    for index, item in enumerate(_mapping_list(frontmatter, "lens-packets")):
        prefix = f"lens-packets[{index}]"
        packet_id = _required_string(item, "id")
        if packet_id in packet_ids:
            raise ValueError(f"{prefix}.id: duplicate packet ID {packet_id}")
        if not packet_id.startswith(f"{run_id}-"):
            raise ValueError(f"{prefix}.id: expected the parent run-id prefix")
        packet_ids.add(packet_id)
        lens = _required_string(item, "lens")
        if lens not in {"memory/context", "epistemic"}:
            raise ValueError(f"{prefix}.lens: expected memory/context or epistemic")
        packet_identity = FileIdentity(
            role=f"lens packet {packet_id}",
            display_path=_required_string(item, "path"),
            path=_state_relative_file(
                _required_string(item, "path"),
                run_dir=run_dir,
                field=f"{prefix}.path",
            ),
            expected_sha256=_required_sha256(item, "sha256"),
        )
        packets.append(
            LensPacket(
                packet_id=packet_id,
                lens=lens,
                identity=packet_identity,
                source_register=_required_string(item, "source-register"),
                canonical_register=_required_string(item, "canonical-register"),
                runtime_baseline_sha256=_required_sha256(
                    item, "runtime-baseline-sha256"
                ),
            )
        )

    returns: list[tuple[str, FileIdentity]] = []
    return_packet_ids: set[str] = set()
    for index, item in enumerate(_mapping_list(frontmatter, "lens-returns")):
        prefix = f"lens-returns[{index}]"
        packet_id = _required_string(item, "packet-id")
        if packet_id not in packet_ids:
            raise ValueError(f"{prefix}.packet-id: unknown packet {packet_id}")
        if packet_id in return_packet_ids:
            raise ValueError(f"{prefix}.packet-id: duplicate return for {packet_id}")
        return_packet_ids.add(packet_id)
        display_path = _required_string(item, "path")
        returns.append(
            (
                packet_id,
                FileIdentity(
                    role=f"lens return {packet_id}",
                    display_path=display_path,
                    path=_state_relative_file(
                        display_path, run_dir=run_dir, field=f"{prefix}.path"
                    ),
                    expected_sha256=_required_sha256(item, "sha256"),
                ),
            )
        )

    accepted_packet_ids = _string_list(frontmatter, "accepted-lens-packets")
    if not set(accepted_packet_ids).issubset(return_packet_ids):
        unknown = sorted(set(accepted_packet_ids) - return_packet_ids)
        raise ValueError(
            "accepted-lens-packets: expected returned packet IDs; "
            f"missing returns for {unknown}"
        )

    corrections = _mapping_list(frontmatter, "corrections")
    packets_by_id = {packet.packet_id: packet for packet in packets}
    correction_ids: set[str] = set()
    invalidated_packets: set[str] = set()
    for index, correction in enumerate(corrections):
        prefix = f"corrections[{index}]"
        correction_id = _required_string(correction, "id")
        if correction_id in correction_ids:
            raise ValueError(f"{prefix}.id: duplicate correction ID {correction_id}")
        if not correction_id.startswith(f"{run_id}-"):
            raise ValueError(f"{prefix}.id: expected the parent run-id prefix")
        correction_ids.add(correction_id)
        invalidated = _string_list(correction, "invalidated-packets")
        replacements = _string_list(correction, "replacement-packets")
        if not {*invalidated, *replacements}.issubset(packet_ids):
            raise ValueError(f"{prefix}: expected only registered packet IDs")
        if set(invalidated).intersection(replacements):
            raise ValueError(
                f"{prefix}: invalidated and replacement packets must be distinct"
            )
        invalidated_packets.update(invalidated)
        from_register = _required_string(correction, "from-canonical-register")
        to_register = _required_string(correction, "to-canonical-register")
        if from_register == to_register:
            raise ValueError(f"{prefix}: correction must advance the canonical register")
        for invalidated_id in invalidated:
            invalidated_packet = packets_by_id[invalidated_id]
            if invalidated_packet.canonical_register != from_register:
                raise ValueError(
                    f"{prefix}: invalidated packet {invalidated_id} does not use "
                    "from-canonical-register"
                )
            if not any(
                packets_by_id[replacement_id].lens == invalidated_packet.lens
                and packets_by_id[replacement_id].canonical_register == to_register
                for replacement_id in replacements
            ):
                raise ValueError(
                    f"{prefix}: no same-lens replacement for {invalidated_id} "
                    "uses to-canonical-register"
                )
        _required_string(correction, "reason")
    if invalidated_packets.intersection(accepted_packet_ids):
        invalid = sorted(invalidated_packets.intersection(accepted_packet_ids))
        raise ValueError(
            f"accepted-lens-packets: invalidated packets cannot be accepted: {invalid}"
        )

    source_register = _optional_string(frontmatter, "source-register")
    canonical_register = _optional_string(frontmatter, "canonical-register")
    runtime_sha256 = (
        None if runtime_baseline is None else runtime_baseline.expected_sha256
    )
    for packet in packets:
        if source_register is not None and packet.source_register != source_register:
            raise ValueError(
                f"lens packet {packet.packet_id}: source-register does not match run state"
            )
        if runtime_sha256 is not None and (
            packet.runtime_baseline_sha256 != runtime_sha256
        ):
            raise ValueError(
                f"lens packet {packet.packet_id}: runtime-baseline-sha256 does not match run state"
            )

    if _PHASES.index(phase) >= _PHASES.index("lenses-issued"):
        issued_lenses = {packet.lens for packet in packets}
        if issued_lenses != {"memory/context", "epistemic"}:
            raise ValueError("lens-packets: both mandatory lenses must be issued")
    if _PHASES.index(phase) >= _PHASES.index("lenses-complete"):
        packet_lens = {packet.packet_id: packet.lens for packet in packets}
        accepted_lenses = {packet_lens[item] for item in accepted_packet_ids}
        if accepted_lenses != {"memory/context", "epistemic"}:
            raise ValueError("accepted-lens-packets: both mandatory lenses must be accepted")
        if canonical_register is not None and not any(
            packet.packet_id in accepted_packet_ids
            and packet.canonical_register == canonical_register
            for packet in packets
        ):
            raise ValueError(
                "canonical-register: no accepted lens packet uses the current register"
            )

    assembled_entry = _assembled_identity(
        frontmatter,
        role="assembled entry",
        path_field="assembled-entry",
        hash_field="assembled-entry-sha256",
        bytes_field="assembled-entry-byte-length",
        repo_root=repo_root,
        carrier=carrier,
    )
    assembled_manifest = _assembled_identity(
        frontmatter,
        role="assembled manifest",
        path_field="assembled-manifest",
        hash_field="assembled-manifest-sha256",
        bytes_field="assembled-manifest-byte-length",
        repo_root=repo_root,
        carrier=carrier,
    )
    if (
        assembled_entry is not None
        and carrier != "response"
        and (canonical_entry is None or assembled_entry.path != canonical_entry)
    ):
        raise ValueError("assembled-entry: expected the canonical-entry path")
    if physical_form == "package" and _PHASES.index(phase) >= _PHASES.index(
        "assembled"
    ):
        if assembled_manifest is None:
            raise ValueError("assembled-manifest: package form requires a manifest")
        if carrier != "response" and (
            canonical_manifest is None
            or assembled_manifest.path != canonical_manifest
        ):
            raise ValueError(
                "assembled-manifest: expected the canonical-manifest path"
            )
    elif assembled_manifest is not None:
        raise ValueError("assembled-manifest: only package form uses a manifest")

    validation_target = _optional_string(frontmatter, "validation-target")
    validation_target_sha256 = _optional_sha256(
        frontmatter, "validation-target-sha256"
    )
    validation_receipt = _file_identity(
        frontmatter,
        role="validation receipt",
        path_field="validation-receipt-path",
        hash_field="validation-receipt-sha256",
        run_dir=run_dir,
    )
    if validation_target is not None and assembled_entry is not None:
        if validation_target != assembled_entry.display_path:
            raise ValueError("validation-target: expected the assembled-entry path")
        if validation_target_sha256 != assembled_entry.expected_sha256:
            raise ValueError(
                "validation-target-sha256: expected the assembled-entry SHA-256"
            )

    handoff_entry_sha256 = _optional_sha256(frontmatter, "handoff-entry-sha256")
    handoff_manifest_sha256 = _optional_sha256(
        frontmatter, "handoff-manifest-sha256"
    )
    if (
        handoff_entry_sha256 is not None
        and assembled_entry is not None
        and handoff_entry_sha256 != assembled_entry.expected_sha256
    ):
        raise ValueError(
            "handoff-entry-sha256: expected the assembled-entry SHA-256"
        )
    if (
        handoff_manifest_sha256 is not None
        and assembled_manifest is not None
        and handoff_manifest_sha256 != assembled_manifest.expected_sha256
    ):
        raise ValueError(
            "handoff-manifest-sha256: expected the assembled-manifest SHA-256"
        )

    return AgenticAnalysisRunState(
        path=state_path,
        run_dir=run_dir,
        frontmatter=frontmatter,
        run_id=run_id,
        phase=phase,
        carrier=carrier,
        physical_form=physical_form,
        source_kind=source_kind,
        source_revision=source_revision,
        source_capture=source_capture,
        source_root=source_root,
        source_register=source_register,
        canonical_register=canonical_register,
        canonical_entry=canonical_entry,
        canonical_manifest=canonical_manifest,
        runtime_baseline=runtime_baseline,
        lens_packets=tuple(packets),
        lens_returns=tuple(returns),
        accepted_packet_ids=accepted_packet_ids,
        corrections=corrections,
        assembled_entry=assembled_entry,
        assembled_manifest=assembled_manifest,
        validation_target=validation_target,
        validation_target_sha256=validation_target_sha256,
        validation_receipt=validation_receipt,
        handoff_entry_sha256=handoff_entry_sha256,
        handoff_manifest_sha256=handoff_manifest_sha256,
    )


def _verify_file(identity: FileIdentity) -> str | None:
    if identity.path.is_symlink() or not identity.path.is_file():
        return f"{identity.role}: missing regular file {identity.display_path}"
    content = identity.path.read_bytes()
    actual_sha256 = sha256(content).hexdigest()
    if actual_sha256 != identity.expected_sha256:
        return (
            f"{identity.role}: SHA-256 mismatch for {identity.display_path}; "
            f"expected {identity.expected_sha256}, got {actual_sha256}"
        )
    if identity.expected_bytes is not None and len(content) != identity.expected_bytes:
        return (
            f"{identity.role}: byte-length mismatch for {identity.display_path}; "
            f"expected {identity.expected_bytes}, got {len(content)}"
        )
    return None


def _verify_lens_header(
    identity: FileIdentity,
    *,
    run_id: str,
    lens: str,
    packet_id: str,
    reviewed_boundary: str | None,
    source_register: str,
    canonical_register: str,
    runtime_baseline_sha256: str,
) -> str | None:
    try:
        content = identity.path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return f"{identity.role}: cannot read packet header: {exc}"
    document, error = parse_document(content)
    frontmatter = None if document is None else document.frontmatter
    if error is not None or frontmatter is None:
        return f"{identity.role}: expected a parseable YAML packet header"
    expected = {
        "run-id": run_id,
        "lens": lens,
        "packet-id": packet_id,
        "reviewed-boundary": reviewed_boundary,
        "source-register": source_register,
        "canonical-register": canonical_register,
        "runtime-baseline-sha256": runtime_baseline_sha256,
    }
    actual = {field: frontmatter.get(field) for field in expected}
    if actual != expected:
        return f"{identity.role}: packet header does not match the run-state identities"
    return None


def verify_agentic_analysis_run_state(
    state: AgenticAnalysisRunState,
) -> tuple[list[str], list[str]]:
    """Return pass and failure messages for all state-owned byte identities."""
    passes: list[str] = []
    failures: list[str] = []
    identities = [
        identity
        for identity in (
            state.source_capture,
            state.runtime_baseline,
            *(packet.identity for packet in state.lens_packets),
            *(identity for _packet_id, identity in state.lens_returns),
            state.assembled_entry,
            state.assembled_manifest,
            state.validation_receipt,
        )
        if identity is not None
    ]
    for identity in identities:
        error = _verify_file(identity)
        if error is None:
            passes.append(
                f"{identity.role}: byte identity matches {identity.display_path}"
            )
        else:
            failures.append(error)

    if state.source_root is not None:
        if state.source_root.is_symlink() or not state.source_root.is_dir():
            failures.append(
                f"source root: missing regular directory {state.source_root}"
            )
        else:
            passes.append(f"source root: frozen root exists at {state.source_root}")

    packet_by_id = {packet.packet_id: packet for packet in state.lens_packets}
    for packet in state.lens_packets:
        if any(
            message.startswith(f"{packet.identity.role}:") for message in failures
        ):
            continue
        error = _verify_lens_header(
            packet.identity,
            run_id=state.run_id,
            lens=packet.lens,
            packet_id=packet.packet_id,
            reviewed_boundary=state.source_revision,
            source_register=packet.source_register,
            canonical_register=packet.canonical_register,
            runtime_baseline_sha256=packet.runtime_baseline_sha256,
        )
        if error is None:
            passes.append(f"{packet.identity.role}: packet header matches run state")
        else:
            failures.append(error)
    for packet_id, identity in state.lens_returns:
        if any(message.startswith(f"{identity.role}:") for message in failures):
            continue
        packet = packet_by_id[packet_id]
        error = _verify_lens_header(
            identity,
            run_id=state.run_id,
            lens=packet.lens,
            packet_id=packet.packet_id,
            reviewed_boundary=state.source_revision,
            source_register=packet.source_register,
            canonical_register=packet.canonical_register,
            runtime_baseline_sha256=packet.runtime_baseline_sha256,
        )
        if error is None:
            passes.append(f"{identity.role}: echoed packet header matches run state")
        else:
            failures.append(error)

    if state.validation_receipt is not None and not any(
        message.startswith("validation receipt:") for message in failures
    ):
        try:
            payload = json.loads(state.validation_receipt.path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            failures.append(f"validation receipt: invalid JSON: {exc}")
        else:
            artifacts = payload.get("analysed_artifacts")
            expected_artifact = {
                "path": state.validation_target,
                "type": "agentic-system-analysis-result",
                "warnings": 0,
                "failures": 0,
            }
            if (
                payload.get("schema") != "commonplace.validation.v1"
                or payload.get("status") != "success"
                or payload.get("summary", {}).get("files_analysed") != 1
                or artifacts != [expected_artifact]
            ):
                failures.append(
                    "validation receipt: expected one successful "
                    "agentic-system-analysis-result and no warnings or failures"
                )
            else:
                passes.append(
                    "validation receipt: one intended agentic-system-analysis-result passed cleanly"
                )

    if state.phase == "handoff-ready" and state.assembled_entry is not None:
        try:
            content = state.assembled_entry.path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            failures.append(f"handoff entry: cannot read result: {exc}")
        else:
            document, error = parse_document(content)
            frontmatter = None if document is None else document.frontmatter
            if error is not None or frontmatter is None:
                failures.append("handoff entry: result frontmatter is not parseable")
            elif frontmatter.get("type") != AGENTIC_ANALYSIS_RESULT_TYPE:
                failures.append(
                    f"handoff entry: expected type {AGENTIC_ANALYSIS_RESULT_TYPE}"
                )
            elif frontmatter.get("run-id") != state.run_id:
                failures.append("handoff entry: result run-id does not match run state")
            else:
                passes.append("handoff entry: type and run-id match the run state")

    return passes, failures
