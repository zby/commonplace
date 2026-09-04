"""Parsing and integrity checks for agentic-system analysis run state."""

from __future__ import annotations

import json
import re
import subprocess
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
_LOCAL_SOURCE_ANCHOR_RE = re.compile(
    r"`(?P<path>[A-Za-z0-9._/-]+\.[A-Za-z0-9._-]+):"
    r"(?P<ranges>[0-9]+(?:-[0-9]+)?(?:,[0-9]+(?:-[0-9]+)?)*)`"
)
_GITHUB_BLOB_ANCHOR_RE = re.compile(
    r"https://github\.com/[^/\s)]+/[^/\s)]+/blob/"
    r"(?P<revision>[0-9a-f]{40}|[0-9a-f]{64})/"
    r"(?P<path>[^\s)#]+)#L(?P<start>[0-9]+)(?:-L(?P<end>[0-9]+))?"
)
_ROUTE_ID_RE = re.compile(r"(?m)^\|\s*(RTE-[A-Za-z0-9_-]+)\s*\|")
_ROUTE_CLOSURE_FIELDS = (
    "route-id",
    "immediate-return",
    "later-read-back",
    "delegated-visibility",
    "selection-predicate",
    "invalidation-or-expiry",
    "activation-or-effect",
    "evidence-and-limits",
)
_DIAGNOSTIC_SUFFIX_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")


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
    runtime_baseline_canonical_register: str | None
    diagnostic_ledger: FileIdentity | None
    lens_return_byte_budget: int
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
    handoff: dict[str, Any] | None


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


def _optional_mapping(values: dict[str, Any], field: str) -> dict[str, Any] | None:
    value = values.get(field)
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError(f"{field}: expected null or a mapping")  # noqa: TRY004
    return value


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
        raise ValueError("source-root: expected an absolute source access root")
    source_capture_path_value = _optional_string(frontmatter, "source-capture-path")
    if source_kind == "checkout" and source_root is not None:
        if source_capture_path_value is None:
            raise ValueError("source-capture-path: expected the checkout source root")
        source_capture_path = Path(source_capture_path_value)
        if not source_capture_path.is_absolute():
            raise ValueError("source-capture-path: expected an absolute checkout path")
        if source_capture_path.resolve(strict=False) != source_root.resolve(strict=False):
            raise ValueError("source-capture-path: expected the same path as source-root")

    run_dir = state_path.parent
    runtime_baseline = _file_identity(
        frontmatter,
        role="runtime baseline",
        path_field="runtime-baseline-path",
        hash_field="runtime-baseline-sha256",
        run_dir=run_dir,
    )
    runtime_baseline_canonical_register = _optional_string(
        frontmatter, "runtime-baseline-canonical-register"
    )
    if runtime_baseline is None and runtime_baseline_canonical_register is not None:
        raise ValueError(
            "runtime-baseline-canonical-register: requires a runtime baseline"
        )
    if runtime_baseline is not None and runtime_baseline_canonical_register is None:
        raise ValueError(
            "runtime-baseline-canonical-register: required with a runtime baseline"
        )
    diagnostic_ledger = _file_identity(
        frontmatter,
        role="diagnostic ledger",
        path_field="diagnostic-ledger-path",
        hash_field="diagnostic-ledger-sha256",
        bytes_field="diagnostic-ledger-byte-length",
        run_dir=run_dir,
    )
    lens_return_byte_budget = frontmatter.get("lens-return-byte-budget")
    if (
        not isinstance(lens_return_byte_budget, int)
        or isinstance(lens_return_byte_budget, bool)
        or lens_return_byte_budget < 1
    ):
        raise ValueError("lens-return-byte-budget: expected a positive integer")

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
            expected_bytes=item.get("byte-length"),
        )
        if (
            not isinstance(packet_identity.expected_bytes, int)
            or isinstance(packet_identity.expected_bytes, bool)
            or packet_identity.expected_bytes < 0
        ):
            raise ValueError(f"{prefix}.byte-length: expected a non-negative integer")
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
                    expected_bytes=item.get("byte-length"),
                ),
            )
        )
        return_bytes = returns[-1][1].expected_bytes
        if (
            not isinstance(return_bytes, int)
            or isinstance(return_bytes, bool)
            or return_bytes < 0
        ):
            raise ValueError(f"{prefix}.byte-length: expected a non-negative integer")
        if return_bytes > lens_return_byte_budget:
            raise ValueError(
                f"{prefix}.byte-length: {return_bytes} exceeds the declared "
                f"lens-return-byte-budget {lens_return_byte_budget}"
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
        if phase == "lenses-complete" and canonical_register is not None and not any(
            packet.packet_id in accepted_packet_ids
            and packet.canonical_register == canonical_register
            for packet in packets
        ):
            raise ValueError(
                "canonical-register: before reconciliation, no accepted lens packet "
                "uses the current register"
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
    handoff = _optional_mapping(frontmatter, "handoff")
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
    if phase == "handoff-ready":
        if handoff is None:
            raise ValueError("handoff: required at handoff-ready")
        lens_runs = _mapping_list(handoff, "lens-runs")
        lenses: set[str] = set()
        for index, lens_run in enumerate(lens_runs):
            prefix = f"handoff.lens-runs[{index}]"
            lens = _required_string(lens_run, "lens")
            if lens not in {"memory/context", "epistemic"}:
                raise ValueError(f"{prefix}.lens: expected memory/context or epistemic")
            if lens in lenses:
                raise ValueError(f"{prefix}.lens: duplicate lens {lens}")
            lenses.add(lens)
            _required_string(lens_run, "scope")
            if _required_string(lens_run, "depth") not in {"brief", "full"}:
                raise ValueError(f"{prefix}.depth: expected brief or full")
        if lenses != {"memory/context", "epistemic"}:
            raise ValueError("handoff.lens-runs: both mandatory lenses are required")
        legacy = _optional_mapping(handoff, "legacy-memory-review")
        if legacy is None:
            raise ValueError("handoff.legacy-memory-review: expected a mapping")
        if _required_string(legacy, "detection") not in {
            "detected",
            "not-detected",
            "unresolved",
        }:
            raise ValueError(
                "handoff.legacy-memory-review.detection: expected detected, "
                "not-detected, or unresolved"
            )
        if _required_string(legacy, "invocation") not in {
            "invoked",
            "not-applicable",
            "not-authorized",
            "blocked",
        }:
            raise ValueError(
                "handoff.legacy-memory-review.invocation: expected invoked, "
                "not-applicable, not-authorized, or blocked"
            )
        _optional_string(legacy, "location")
        _required_string(legacy, "validation")
        transfer = _optional_mapping(handoff, "transfer-scan")
        if transfer is None:
            raise ValueError("handoff.transfer-scan: expected a mapping")
        if _required_string(transfer, "disposition") not in {
            "not-requested",
            "response",
            "state",
            "blocked",
        }:
            raise ValueError(
                "handoff.transfer-scan.disposition: expected not-requested, "
                "response, state, or blocked"
            )
        _optional_string(transfer, "location")
        _required_string(handoff, "retention-disposition")
        _string_list(handoff, "limitations")
        _string_list(handoff, "blockers")
    elif handoff is not None:
        raise ValueError("handoff: only handoff-ready phase may set it")

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
        runtime_baseline_canonical_register=runtime_baseline_canonical_register,
        diagnostic_ledger=diagnostic_ledger,
        lens_return_byte_budget=lens_return_byte_budget,
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
        handoff=handoff,
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


def _markdown_section(content: str, heading: str) -> str | None:
    match = re.search(
        rf"(?ms)^## {re.escape(heading)}\s*$\n(?P<body>.*?)(?=^## |\Z)",
        content,
    )
    return None if match is None else match.group("body")


def _verify_runtime_baseline(
    identity: FileIdentity,
    *,
    run_id: str,
    reviewed_boundary: str | None,
    source_register: str | None,
    canonical_register: str | None,
) -> tuple[list[str], list[str]]:
    passes: list[str] = []
    failures: list[str] = []
    try:
        content = identity.path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return passes, [f"runtime baseline: cannot read structured header: {exc}"]

    document, error = parse_document(content)
    frontmatter = None if document is None else document.frontmatter
    if error is not None or frontmatter is None:
        return passes, ["runtime baseline: expected a parseable YAML header"]

    expected_header = {
        "run-id": run_id,
        "reviewed-boundary": reviewed_boundary,
        "source-register": source_register,
        "canonical-register": canonical_register,
    }
    actual_header = {field: frontmatter.get(field) for field in expected_header}
    if actual_header != expected_header:
        failures.append(
            "runtime baseline: header does not match the run-state identities"
        )

    raw_closures = frontmatter.get("route-closure")
    if not isinstance(raw_closures, list) or not raw_closures:
        failures.append("runtime baseline: route-closure must be a non-empty list")
        return passes, failures

    closure_ids: list[str] = []
    for index, closure in enumerate(raw_closures):
        prefix = f"runtime baseline route-closure[{index}]"
        if not isinstance(closure, dict):
            failures.append(f"{prefix}: expected a mapping")
            continue
        for field in _ROUTE_CLOSURE_FIELDS:
            value = closure.get(field)
            if not isinstance(value, str) or not value.strip():
                failures.append(f"{prefix}.{field}: expected a non-empty string")
        route_id = closure.get("route-id")
        if isinstance(route_id, str) and route_id.strip():
            closure_ids.append(route_id)

    duplicate_ids = sorted(
        {route_id for route_id in closure_ids if closure_ids.count(route_id) > 1}
    )
    if duplicate_ids:
        failures.append(
            "runtime baseline: duplicate route-closure IDs "
            + ", ".join(duplicate_ids)
        )

    route_section = _markdown_section(content, "Canonical routes")
    if route_section is None:
        failures.append("runtime baseline: missing ## Canonical routes section")
        return passes, failures
    canonical_route_ids = set(_ROUTE_ID_RE.findall(route_section))
    if not canonical_route_ids:
        failures.append(
            "runtime baseline: ## Canonical routes contains no RTE-* table rows"
        )
        return passes, failures

    closure_id_set = set(closure_ids)
    missing = sorted(canonical_route_ids - closure_id_set)
    unknown = sorted(closure_id_set - canonical_route_ids)
    if missing:
        failures.append(
            "runtime baseline: route-closure omits canonical routes "
            + ", ".join(missing)
        )
    if unknown:
        failures.append(
            "runtime baseline: route-closure names unknown routes "
            + ", ".join(unknown)
        )
    if not failures:
        passes.append(
            "runtime baseline: header matches run state and route closure covers "
            f"all {len(canonical_route_ids)} canonical routes"
        )
    return passes, failures


def _git_blob_lines(
    *, source_root: Path, revision: str, source_path: str
) -> tuple[int | None, str | None]:
    pure = PurePosixPath(source_path)
    if (
        pure.is_absolute()
        or source_path != pure.as_posix()
        or ".." in pure.parts
        or not pure.parts
    ):
        return None, "expected a normalized commit-relative path"
    try:
        blob = subprocess.run(
            [
                "git",
                "--no-replace-objects",
                "-C",
                str(source_root),
                "show",
                f"{revision}:{source_path}",
            ],
            check=False,
            capture_output=True,
        )
    except OSError as exc:
        return None, f"could not invoke git: {exc}"
    if blob.returncode != 0:
        return None, "path does not resolve to a blob at the recorded commit"
    try:
        content = blob.stdout.decode("utf-8")
    except UnicodeDecodeError:
        return None, "cited blob is not UTF-8 text"
    return len(content.splitlines()), None


def _parse_line_ranges(value: str) -> tuple[tuple[int, int], ...]:
    ranges: list[tuple[int, int]] = []
    for item in value.split(","):
        start_text, separator, end_text = item.partition("-")
        start = int(start_text)
        end = int(end_text) if separator else start
        ranges.append((start, end))
    return tuple(ranges)


def _verify_source_anchors(
    content: str, *, source_root: Path, source_revision: str
) -> tuple[list[str], list[str]]:
    passes: list[str] = []
    failures: list[str] = []
    anchors: dict[tuple[str, tuple[tuple[int, int], ...]], set[str]] = {}

    for match in _LOCAL_SOURCE_ANCHOR_RE.finditer(content):
        key = (match.group("path"), _parse_line_ranges(match.group("ranges")))
        anchors.setdefault(key, set()).add("local")
    for match in _GITHUB_BLOB_ANCHOR_RE.finditer(content):
        revision = match.group("revision")
        source_path = match.group("path")
        start = int(match.group("start"))
        end = int(match.group("end") or start)
        key = (source_path, ((start, end),))
        anchors.setdefault(key, set()).add("GitHub")
        if revision != source_revision:
            failures.append(
                "source citation: GitHub anchor uses revision "
                f"{revision}, expected {source_revision}: {source_path}"
            )

    for (source_path, line_ranges), kinds in sorted(anchors.items()):
        line_count, error = _git_blob_lines(
            source_root=source_root,
            revision=source_revision,
            source_path=source_path,
        )
        if error is not None or line_count is None:
            failures.append(f"source citation: {source_path}: {error}")
            continue
        invalid_ranges = [
            (start, end)
            for start, end in line_ranges
            if start < 1 or end < start or end > line_count
        ]
        if invalid_ranges:
            rendered = ", ".join(
                str(start) if start == end else f"{start}-{end}"
                for start, end in invalid_ranges
            )
            failures.append(
                f"source citation: {source_path}: line range {rendered} is outside "
                f"the recorded blob's 1-{line_count} lines"
            )
            continue
        passes.append(
            f"source citation: {source_path} and {len(line_ranges)} line range(s) "
            f"resolve at the recorded commit ({'/'.join(sorted(kinds))})"
        )

    return passes, failures


def _verify_diagnostic_ledger(
    state: AgenticAnalysisRunState,
) -> tuple[list[str], list[str]]:
    identity = state.diagnostic_ledger
    if identity is None:
        return [], ["diagnostic ledger: missing byte identity"]
    try:
        content = identity.path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [], [f"diagnostic ledger: cannot read JSON Lines: {exc}"]

    passes: list[str] = []
    failures: list[str] = []
    records: list[dict[str, Any]] = []
    ids: set[str] = set()
    for line_number, line in enumerate(content.splitlines(), start=1):
        if not line.strip():
            failures.append(
                f"diagnostic ledger line {line_number}: blank lines are not allowed"
            )
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            failures.append(
                f"diagnostic ledger line {line_number}: invalid JSON: {exc.msg}"
            )
            continue
        if not isinstance(record, dict):
            failures.append(
                f"diagnostic ledger line {line_number}: expected a JSON object"
            )
            continue
        records.append(record)
        prefix = f"diagnostic ledger line {line_number}"
        record_id = record.get("id")
        if (
            not isinstance(record_id, str)
            or not record_id.startswith(f"{state.run_id}-DIAG-")
            or not _DIAGNOSTIC_SUFFIX_RE.fullmatch(
                record_id.removeprefix(f"{state.run_id}-DIAG-")
            )
        ):
            failures.append(f"{prefix}.id: expected {state.run_id}-DIAG-<suffix>")
        elif record_id in ids:
            failures.append(f"{prefix}.id: duplicate diagnostic ID {record_id}")
        else:
            ids.add(record_id)

        for field in ("producer", "operation", "working-directory"):
            value = record.get(field)
            if not isinstance(value, str) or not value.strip():
                failures.append(f"{prefix}.{field}: expected a non-empty string")
        working_directory = record.get("working-directory")
        if isinstance(working_directory, str) and not Path(working_directory).is_absolute():
            failures.append(f"{prefix}.working-directory: expected an absolute path")

        phase = record.get("phase")
        if phase not in _PHASES:
            failures.append(f"{prefix}.phase: expected a run-state phase")
        elif _PHASES.index(phase) > _PHASES.index(state.phase):
            failures.append(f"{prefix}.phase: cannot be later than the run state")

        outcome = record.get("outcome")
        if not isinstance(outcome, str) or outcome not in {
            "failed",
            "truncated",
            "non-executed",
        }:
            failures.append(
                f"{prefix}.outcome: expected failed, truncated, or non-executed"
            )
        classification = record.get("classification")
        if not isinstance(classification, str) or classification not in {
            "tool-failure",
            "execution-error",
            "expected-invalidation",
            "environmental-condition",
            "source-conflict",
            "harness-error",
        }:
            failures.append(
                f"{prefix}.classification: expected a registered diagnostic class"
            )
        exit_status = record.get("exit-status")
        if exit_status is not None and (
            not isinstance(exit_status, int) or isinstance(exit_status, bool)
        ):
            failures.append(f"{prefix}.exit-status: expected an integer or null")
        disposition = record.get("disposition")
        if not isinstance(disposition, str) or disposition not in {
            "recovered",
            "unresolved",
            "non-evidentiary",
        }:
            failures.append(
                f"{prefix}.disposition: expected recovered, unresolved, or non-evidentiary"
            )
        if not isinstance(record.get("material"), bool):
            failures.append(f"{prefix}.material: expected a boolean")
        environment = record.get("relevant-environment")
        if not isinstance(environment, list) or any(
            not isinstance(item, str) or not item.strip() for item in environment
        ):
            failures.append(
                f"{prefix}.relevant-environment: expected a list of non-empty strings"
            )
        recovery = record.get("recovery")
        if disposition == "recovered" and (
            not isinstance(recovery, str) or not recovery.strip()
        ):
            failures.append(f"{prefix}.recovery: required for recovered diagnostics")
        if disposition != "recovered" and recovery is not None:
            failures.append(
                f"{prefix}.recovery: allowed only for recovered diagnostics"
            )

        exact_output = record.get("exact-output")
        output_path = record.get("output-path")
        if (isinstance(exact_output, str) and exact_output) == (
            isinstance(output_path, str) and bool(output_path)
        ):
            failures.append(
                f"{prefix}: set exactly one of exact-output or output-path"
            )
        if isinstance(output_path, str) and output_path:
            output_identity_values = {
                "path": output_path,
                "sha256": record.get("output-sha256"),
                "bytes": record.get("output-byte-length"),
            }
            try:
                output_identity = _file_identity(
                    output_identity_values,
                    role=f"diagnostic output {record_id or line_number}",
                    path_field="path",
                    hash_field="sha256",
                    bytes_field="bytes",
                    run_dir=state.run_dir,
                )
            except ValueError as exc:
                failures.append(f"{prefix}: {exc}")
            else:
                if output_identity is not None:
                    error = _verify_file(output_identity)
                    if error is not None:
                        failures.append(error)

    unresolved_material_ids = {
        record["id"]
        for record in records
        if isinstance(record.get("id"), str)
        and record.get("material") is True
        and record.get("disposition") == "unresolved"
    }
    if unresolved_material_ids and state.assembled_entry is not None:
        try:
            result_content = state.assembled_entry.path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            result_content = ""
        unreported = sorted(
            item for item in unresolved_material_ids if item not in result_content
        )
        if unreported:
            failures.append(
                "diagnostic ledger: unresolved material diagnostics are not named "
                "in the assembled result: "
                + ", ".join(unreported)
            )

    if not failures:
        passes.append(
            f"diagnostic ledger: {len(records)} structured record(s) verified"
        )
    return passes, failures


def render_agentic_analysis_handoff(state: AgenticAnalysisRunState) -> str:
    """Render the complete operator handoff from checked run and result state."""
    if state.phase != "handoff-ready" or state.handoff is None:
        raise ValueError("operator handoff requires a handoff-ready run state")
    if state.assembled_entry is None:
        raise ValueError("operator handoff requires an assembled entry")
    try:
        content = state.assembled_entry.path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"operator handoff cannot read the result: {exc}") from exc
    document, error = parse_document(content)
    frontmatter = None if document is None else document.frontmatter
    if error is not None or frontmatter is None:
        raise ValueError("operator handoff requires parseable result frontmatter")

    handoff = state.handoff
    lens_runs = handoff["lens-runs"]
    legacy = handoff["legacy-memory-review"]
    transfer = handoff["transfer-scan"]
    consumers = ", ".join(state.frontmatter["canonical-consumers"])
    projections = state.frontmatter["permitted-projections"]
    projection_text = ", ".join(projections) if projections else "none"
    if state.carrier == "response":
        result_location = "response stable block"
    else:
        result_location = (
            f"[{state.assembled_entry.display_path}]"
            f"(<{state.assembled_entry.path.as_posix()}>)"
        )
    lens_text = "; ".join(
        f"{item['lens']}: {item['depth']} over {item['scope']}" for item in lens_runs
    )
    legacy_location = legacy["location"] or "none"
    transfer_location = transfer["location"] or "none"
    receipt_text = (
        "none"
        if state.validation_receipt is None
        else (
            f"{state.validation_receipt.display_path} "
            f"(SHA-256 {state.validation_receipt.expected_sha256})"
        )
    )
    limitations = handoff["limitations"]
    blockers = handoff["blockers"]
    limitation_text = "; ".join(limitations) if limitations else "none"
    blocker_text = "; ".join(blockers) if blockers else "none"

    lines = [
        f"# Agentic-system analysis handoff — {state.run_id}",
        "",
        f"**Result:** {result_location}",
        "",
        (
            f"**System and disposition:** {frontmatter.get('system', 'unknown')} — "
            f"{frontmatter.get('result-disposition', 'unknown')}"
        ),
        "",
        (
            f"**Lifecycle:** consumers: {consumers}; carrier: {state.carrier}; "
            f"physical form: {state.physical_form}; retention: "
            f"{state.frontmatter['retention-rule']}; cleanup: "
            f"{state.frontmatter['cleanup-condition']}; permitted projections: "
            f"{projection_text}"
        ),
        "",
        (
            f"**Boundary:** target class: {frontmatter.get('target-class')}; kind: "
            f"{frontmatter.get('boundary-kind')}; revision: {state.source_revision}; "
            f"tier: {frontmatter.get('evidence-tier')}"
        ),
        "",
        f"**Lens runs:** {lens_text}",
        "",
        (
            f"**Legacy memory review:** detection: {legacy['detection']}; "
            f"invocation: {legacy['invocation']}; location: {legacy_location}; "
            f"validation: {legacy['validation']}"
        ),
        "",
        (
            f"**Stable-result verification:** entry SHA-256 "
            f"{state.handoff_entry_sha256}; validation receipt: {receipt_text}"
        ),
        "",
        f"**Transfer scan:** {transfer['disposition']}; location: {transfer_location}",
        "",
        f"**Retention disposition:** {handoff['retention-disposition']}",
        "",
        f"**Limitations:** {limitation_text}",
        "",
        f"**Blockers:** {blocker_text}",
    ]
    return "\n".join(lines)


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
            state.diagnostic_ledger,
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

    if state.diagnostic_ledger is not None and not any(
        message.startswith("diagnostic ledger:") for message in failures
    ):
        diagnostic_passes, diagnostic_failures = _verify_diagnostic_ledger(state)
        passes.extend(diagnostic_passes)
        failures.extend(diagnostic_failures)

    if state.runtime_baseline is not None and not any(
        message.startswith("runtime baseline:") for message in failures
    ):
        baseline_passes, baseline_failures = _verify_runtime_baseline(
            state.runtime_baseline,
            run_id=state.run_id,
            reviewed_boundary=state.source_revision,
            source_register=state.source_register,
            canonical_register=state.runtime_baseline_canonical_register,
        )
        passes.extend(baseline_passes)
        failures.extend(baseline_failures)

    if state.source_root is not None:
        if state.source_root.is_symlink() or not state.source_root.is_dir():
            failures.append(
                f"source root: missing regular directory {state.source_root}"
            )
        else:
            passes.append(f"source root: access root exists at {state.source_root}")
            if state.source_kind == "checkout" and state.source_revision is not None:
                try:
                    resolved_commit = subprocess.run(
                        [
                            "git",
                            "--no-replace-objects",
                            "-C",
                            str(state.source_root),
                            "rev-parse",
                            "--verify",
                            f"{state.source_revision}^{{commit}}",
                        ],
                        check=False,
                        capture_output=True,
                        text=True,
                    )
                except OSError as exc:
                    failures.append(
                        f"source checkout: could not invoke git for "
                        f"{state.source_root}: {exc}"
                    )
                else:
                    actual_commit = resolved_commit.stdout.strip()
                    if resolved_commit.returncode != 0 or actual_commit != state.source_revision:
                        failures.append(
                            "source checkout: recorded commit does not resolve from "
                            f"{state.source_root}: {state.source_revision}"
                        )
                    else:
                        passes.append(
                            "source checkout: recorded commit resolves independently "
                            f"of HEAD at {state.source_revision}"
                        )

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
                if state.handoff is not None:
                    result_disposition = frontmatter.get("result-disposition")
                    blockers = state.handoff["blockers"]
                    if result_disposition == "complete" and blockers:
                        failures.append(
                            "handoff: a complete result cannot report blockers"
                        )
                    if result_disposition == "blocked" and not blockers:
                        failures.append(
                            "handoff: a blocked result must report at least one blocker"
                        )
                    legacy = state.handoff["legacy-memory-review"]
                    if (
                        legacy["invocation"] == "invoked"
                        and legacy["location"] is None
                    ):
                        failures.append(
                            "handoff: an invoked legacy memory review requires a location"
                        )
                    if (
                        legacy["detection"] == "not-detected"
                        and legacy["invocation"] != "not-applicable"
                    ):
                        failures.append(
                            "handoff: a not-detected legacy memory review must be not-applicable"
                        )
                    if (
                        legacy["detection"] == "detected"
                        and legacy["invocation"] == "not-applicable"
                    ):
                        failures.append(
                            "handoff: a detected legacy memory review cannot be not-applicable"
                        )
                    transfer = state.handoff["transfer-scan"]
                    if (
                        transfer["disposition"] == "state"
                        and transfer["location"] is None
                    ):
                        failures.append(
                            "handoff: a state transfer scan requires a location"
                        )
                if (
                    state.source_kind == "checkout"
                    and state.source_root is not None
                    and state.source_revision is not None
                ):
                    anchor_passes, anchor_failures = _verify_source_anchors(
                        content,
                        source_root=state.source_root,
                        source_revision=state.source_revision,
                    )
                    passes.extend(anchor_passes)
                    failures.extend(anchor_failures)

    return passes, failures
