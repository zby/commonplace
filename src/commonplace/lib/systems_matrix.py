"""Read memory comparisons directly from retained analysis sets."""

from __future__ import annotations

import csv
import io
import json
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

from commonplace.lib.agentic_records import is_absence, set_record_errors
from commonplace.lib.agentic_set import current_analyses

__all__ = [
    "AXES",
    "csv_text",
    "load_results",
    "profile_member_comparison",
    "validate_comparison",
]
AXES = {
    "storage_substrate": {
        "files",
        "repo",
        "sqlite",
        "rdbms",
        "vector",
        "graph",
        "kv",
        "in-memory",
        "prompt-registry",
        "model-weights",
        "service-object",
    },
    "representational_form": {"natural-language", "symbolic", "parametric"},
    "lineage": {"authored", "imported", "trace-extracted", "other-compiled"},
    "behavioral_authority": {
        "knowledge",
        "instruction",
        "enforcement",
        "routing",
        "validation",
        "ranking",
        "learning",
    },
    "write_agency": {"manual", "automatic"},
    "curation_operations": {
        "consolidate",
        "dedup",
        "evolve",
        "synthesize",
        "invalidate",
        "decay",
        "promote",
    },
    "read_back_direction": {"pull", "push"},
    "read_back_signal": {
        "coarse",
        "identifier",
        "inferred-lexical",
        "inferred-embedding",
        "inferred-judgment",
    },
    "trace_learning": {"yes", "no"},
    "trace_source": {"session-logs", "tool-traces", "event-streams", "trajectories"},
}
ASSESSMENTS = {
    "known",
    "partial",
    "absent",
    "inapplicable",
    "uninspected",
    "not-determinable",
}
BASES = {"claimed", "afforded", "wired", "observed", "causally supported"}
METADATA = [
    "system_name",
    "review_file",
    "review_sha256",
    "artifact_file",
    "artifact_sha256",
    "analysis_run",
    "source_identity",
    "reviewed_revision",
    "analysis_cutoff",
    "source_tier",
    "boundary_kind",
    "comparison_scope",
    "one_line",
]
COLUMNS = METADATA + [
    name + suffix
    for name in AXES
    for suffix in ("", "_assessment", "_evidence", "_records")
]


def _strings(value: object, label: str) -> list[str]:
    if not isinstance(value, list) or any(
        not isinstance(v, str) or not v.strip() for v in value
    ):
        raise ValueError(f"{label}: expected a list of nonempty strings")
    if len(value) != len(set(value)):
        raise ValueError(f"{label}: duplicate values")
    return value


def validate_comparison(profile: object, *, known_ids: set[str]) -> dict:
    """Validate authored assessments and references, without classifying prose.

    ``known_ids`` are the record IDs the profile may cite.
    """
    if not isinstance(profile, dict) or set(profile) != {"scope", "axes"}:
        raise ValueError("memory-comparison requires exactly scope and axes")
    if not isinstance(profile["scope"], str) or not profile["scope"].strip():
        raise ValueError(
            "memory-comparison.scope must name the compared memory boundary"
        )
    axes = profile["axes"]
    if not isinstance(axes, dict) or set(axes) != set(AXES):
        raise ValueError(
            "memory-comparison.axes must contain every registered axis exactly once"
        )
    ids = known_ids
    for name, vocabulary in AXES.items():
        entry = axes[name]
        if not isinstance(entry, dict) or set(entry) != {
            "assessment",
            "evidence",
            "values",
            "records",
            "note",
        }:
            raise ValueError(
                f"{name}: requires assessment, evidence, values, records, and note"
            )
        values = _strings(entry["values"], name + ".values")
        records = _strings(entry["records"], name + ".records")
        if (
            not isinstance(entry["assessment"], str)
            or entry["assessment"] not in ASSESSMENTS
        ):
            raise ValueError(f"{name}: invalid assessment")
        if not isinstance(entry["note"], str) or not entry["note"].strip():
            raise ValueError(f"{name}: missing rationale or conclusion prevented")
        if not set(records) <= ids:
            raise ValueError(f"{name}: unresolved records")
        if not set(values) <= vocabulary:
            raise ValueError(f"{name}: off-vocabulary values")
        evidence = entry["evidence"]
        if entry["assessment"] in {"known", "partial"}:
            if not values or not records:
                raise ValueError(
                    f"{name}: known assessment needs values and records; partial does too"
                )
        elif values:
            raise ValueError(f"{name}: non-positive assessment requires empty values")
        if not isinstance(evidence, dict) or set(evidence) != set(values):
            raise ValueError(f"{name}: evidence must cover exactly the declared values")
        for value, support in evidence.items():
            if not isinstance(support, dict) or set(support) != {
                "basis",
                "records",
                "note",
            }:
                raise ValueError(f"{name}.{value}: requires basis, records, and note")
            if not isinstance(support["basis"], str) or support["basis"] not in BASES:
                raise ValueError(f"{name}.{value}: invalid evidence basis")
            refs = _strings(support["records"], f"{name}.{value}.records")
            if not refs or not set(refs) <= ids:
                raise ValueError(f"{name}.{value}: unresolved records")
            if not isinstance(support["note"], str) or not support["note"].strip():
                raise ValueError(f"{name}.{value}: missing evidence rationale")
        if (
            entry["assessment"] == "partial"
            and name == "trace_learning"
            and values == ["no"]
        ):
            raise ValueError(f"{name}: partial coverage cannot establish no")
        if entry["assessment"] == "absent" and not any(is_absence(r) for r in records):
            raise ValueError(f"{name}: absence requires an evidenced-absence record")
        if name == "trace_learning" and len(values) > 1:
            raise ValueError(f"{name}: yes and no cannot be combined")
    trace = axes["trace_learning"]
    if (
        trace["assessment"] == "known"
        and trace["values"] == ["no"]
        and axes["trace_source"]["assessment"] != "inapplicable"
    ):
        raise ValueError(
            "trace_source: must be inapplicable when trace learning is no"
        )
    direction = axes["read_back_direction"]
    if (
        direction["assessment"] == "known"
        and "push" not in direction["values"]
        and axes["read_back_signal"]["assessment"] != "inapplicable"
    ):
        raise ValueError(
            "read_back_signal: must be inapplicable for pull-only read-back"
        )
    return profile


def profile_member_comparison(metadata: dict, *, record_bodies: dict[str, str]) -> dict:
    """Resolve profile support against canonical declarations in record members."""
    known, errors = set_record_errors(record_bodies)
    if errors:
        raise ValueError("; ".join(errors))
    return validate_comparison(metadata.get("memory-comparison"), known_ids=known)


@dataclass(frozen=True)
class MatrixInputs:
    rows: list[dict[str, str]]
    hashes: dict[str, str]


def load_results(root: Path, review_paths: list[Path] | None = None) -> MatrixInputs:
    """Select explicit current overviews, or all current analyses; fail on gaps.

    The shared enumerator validates membership and manifest hashes. Identity
    comes from the overview and comparison data from the profile member.
    """
    from commonplace.lib.validation import ValidationRun

    root = root.resolve()
    run = ValidationRun(root, ())
    sets = current_analyses(root, run=run)
    selected = None if review_paths is None else {(root / path).resolve() for path in review_paths}
    available = {member_set.overview.path for member_set in sets}
    if selected is not None and not selected <= available:
        raise ValueError("selected path is not a current analysis overview")
    rows, hashes = [], {}
    for member_set in sets:
        path = member_set.overview.path
        if selected is not None and path not in selected:
            continue
        relative = path.relative_to(root)
        review_bytes = member_set.overview.content
        manifest_path = member_set.artifact.path / "ARTIFACT.yaml"
        retained = manifest_path.relative_to(root)
        manifest_hash = sha256(member_set.artifact.content).hexdigest()
        data = member_set.overview.frontmatter
        source = member_set.memory.frontmatter["source-identity"]
        meta = {**data, "analysis-run": data["run-id"]}
        member = member_set.profile
        assert member is not None  # complete sets require the separate profile
        profile = profile_member_comparison(member.frontmatter, record_bodies={
            document.name: document.body for document in member_set.documents
            if document.name != "memory-profile.md"
        })
        tier = data.get("evidence-tier")
        if tier not in {"code-grounded", "doc-grounded"}:
            raise ValueError(f"invalid evidence tier: {retained}")
        row = dict(
            zip(
                METADATA,
                [
                    str(data["system"]),
                    relative.as_posix(),
                    sha256(review_bytes).hexdigest(),
                    retained.as_posix(),
                    manifest_hash,
                    meta["analysis-run"],
                    source,
                    str(data["reviewed-boundary"]),
                    str(data["analysis-cutoff"]),
                    tier,
                    str(data["boundary-kind"]),
                    profile["scope"],
                    str(meta.get("description", "")),
                ],
            )
        )
        for name, entry in profile["axes"].items():
            row[name] = sorted(entry["values"])
            row[name + "_assessment"] = entry["assessment"]
            row[name + "_evidence"] = entry["evidence"]
            row[name + "_records"] = list(entry["records"])
        rows.append(row)
        hashes[relative.as_posix()] = row["review_sha256"]
        hashes[retained.as_posix()] = manifest_hash
        for document in member_set.documents:
            hashes[(retained.parent / document.name).as_posix()] = document.sha256
    if not rows:
        raise ValueError("no current analyses selected")
    return MatrixInputs(
        sorted(
            rows, key=lambda row: (row["system_name"].casefold(), row["analysis_run"])
        ),
        hashes,
    )


STRONG_BASES = {"wired", "observed", "causally supported"}


def supported_values(row: dict, axis: str) -> set[str]:
    """Positive implementation evidence, counted once per value and system."""
    if row["source_tier"] != "code-grounded":
        return set()
    return {
        value
        for value, support in row[axis + "_evidence"].items()
        if support["basis"] in STRONG_BASES
    }


def complete_values(row: dict, axis: str) -> tuple[str, ...] | None:
    """A complete strong profile, or None; a filtered subset is not a full profile.

    An evidenced absence is the empty profile.
    """
    if row["source_tier"] != "code-grounded":
        return None
    if row[axis + "_assessment"] == "absent":
        return ()
    values = set(row[axis])
    if row[axis + "_assessment"] == "known" and values == supported_values(row, axis):
        return tuple(sorted(values))
    return None


def csv_row(row: dict) -> dict[str, str]:
    """Serialize one structured row; JSON cells exist only in the CSV file."""
    out = {name: row[name] for name in METADATA}
    for axis in AXES:
        out[axis] = json.dumps(row[axis], separators=(",", ":"))
        out[axis + "_assessment"] = row[axis + "_assessment"]
        out[axis + "_evidence"] = json.dumps(
            row[axis + "_evidence"], sort_keys=True, separators=(",", ":")
        )
        out[axis + "_records"] = ";".join(row[axis + "_records"])
    return out


def csv_text(inputs: MatrixInputs) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(csv_row(row) for row in inputs.rows)
    return output.getvalue()
