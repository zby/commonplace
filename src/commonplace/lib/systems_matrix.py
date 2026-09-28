"""Read memory comparisons directly from retained analysis sets."""

from __future__ import annotations

import csv
import io
import json
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

from commonplace.lib.agentic_records import annotated_ids, declared_ids
from commonplace.lib.agentic_set import (
    RETAINED_ROOT,
    REVIEWS_ROOT,
    RUN_ID,
    is_review_path,
    load_member_set,
    retained_artifact_path,
)
from commonplace.lib.note_parser import parse_document

__all__ = [
    "AXES",
    "RETAINED_ROOT",
    "RUN_ID",
    "csv_text",
    "load_results",
    "memory_member_comparison",
    "retained_artifact_path",
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
    "learning_scope": {"per-task", "per-project", "cross-task"},
    "learning_timing": {"online", "offline", "staged"},
    "distilled_form": {"natural-language", "symbolic", "parametric"},
    "faithfulness_tested": {"yes", "no"},
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


def validate_comparison(
    profile: object, *, known_ids: set[str], memory_report: bool = False
) -> dict:
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
            label = "shared or proposed" if memory_report else "canonical"
            raise ValueError(f"{name}: unresolved {label} records")
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
                label = "shared or proposed" if memory_report else "canonical"
                raise ValueError(f"{name}.{value}: unresolved {label} records")
            if not isinstance(support["note"], str) or not support["note"].strip():
                raise ValueError(f"{name}.{value}: missing evidence rationale")
        if (
            entry["assessment"] == "partial"
            and name in {"trace_learning", "faithfulness_tested"}
            and values == ["no"]
        ):
            raise ValueError(f"{name}: partial coverage cannot establish no")
        if entry["assessment"] == "absent" and not any(
            r.startswith("ABS-") or (memory_report and r.startswith("MEM-ABS-"))
            for r in records
        ):
            raise ValueError(f"{name}: absence requires an evidenced-absence record")
        if name in {"trace_learning", "faithfulness_tested"} and len(values) > 1:
            raise ValueError(f"{name}: yes and no cannot be combined")
    trace = axes["trace_learning"]
    if trace["assessment"] == "known" and trace["values"] == ["no"]:
        for name in (
            "trace_source",
            "learning_scope",
            "learning_timing",
            "distilled_form",
        ):
            if axes[name]["assessment"] != "inapplicable":
                raise ValueError(
                    f"{name}: must be inapplicable when trace learning is no"
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
    faithfulness = axes["faithfulness_tested"]
    if faithfulness["values"] == ["yes"] and faithfulness["evidence"]["yes"][
        "basis"
    ] not in {
        "observed",
        "causally supported",
    }:
        raise ValueError("faithfulness_tested: yes requires execution evidence")
    return profile


def memory_member_comparison(metadata: dict, body: str) -> dict:
    """Validate a memory report's own ``memory-comparison`` and return it.

    The one profile check shared by the memory type's validation rule and
    the comparison loader. Either regime cites seeded records through its
    ``On <ID>`` annotations; the local report also declares proposals, the
    finalized member declares their canonical records.
    """
    finalized = isinstance(metadata.get("finalized-from"), str)
    known = annotated_ids(body) | set(declared_ids(body, proposals=not finalized))
    return validate_comparison(
        metadata.get("memory-comparison"), known_ids=known, memory_report=not finalized
    )


@dataclass(frozen=True)
class MatrixInputs:
    rows: list[dict[str, str]]
    hashes: dict[str, str]


def load_results(root: Path, review_paths: list[Path] | None = None) -> MatrixInputs:
    """Select explicit main reviews, or all generated main reviews; fail on gaps.

    Each review pins the manifest of a validated retained directory artifact.
    Identity comes from its overview and the comparison profile from memory.md.
    """
    from commonplace.lib.validation import ValidationRun

    root = root.resolve()
    run = ValidationRun(root, ())
    paths = (
        review_paths
        if review_paths is not None
        else sorted((root / REVIEWS_ROOT).glob("*.md"))
    )
    rows, hashes, identities = [], {}, set()
    for raw_path in paths:
        path = (root / raw_path).resolve()
        relative = path.relative_to(root)
        if not is_review_path(relative.as_posix()):
            raise ValueError(f"not a main-review path: {raw_path}")
        review_bytes = path.read_bytes()
        review, error = parse_document(review_bytes.decode("utf-8"))
        if error or review is None:
            raise ValueError(f"{relative}: malformed Markdown")
        meta = review.frontmatter or {}
        if meta.get("generated-by") != "analyse-agentic-system":
            if review_paths is not None:
                raise ValueError(f"not a generated main review: {relative}")
            continue
        retained = retained_artifact_path(meta.get("analysis-run"))
        if meta.get("analysis-artifact") != retained.as_posix():
            raise ValueError(
                f"{relative}: missing or mismatched retained manifest; regenerate the main review"
            )
        manifest_path = (root / retained).resolve()
        if manifest_path.relative_to(root) != retained:
            raise ValueError(f"retained manifest must use its canonical path: {retained}")
        manifest_bytes = run.read_bytes(manifest_path)
        manifest_hash = sha256(manifest_bytes).hexdigest()
        if meta.get("analysis-artifact-sha256") != manifest_hash:
            raise ValueError(f"retained manifest SHA-256 mismatch: {retained}")
        try:
            member_set = load_member_set(manifest_path.parent, run=run)
        except ValueError as exc:
            raise ValueError(f"{retained}: {exc}") from exc
        data = member_set.overview.frontmatter
        if data.get("result-disposition") != "complete":
            raise ValueError(f"not a complete analysis overview: {retained}")
        if data.get("run-id") != meta["analysis-run"] or data.get(
            "reviewed-boundary"
        ) != meta.get("reviewed-revision"):
            raise ValueError(f"review/overview identity mismatch: {relative}")
        source = meta.get("source-identity")
        if not isinstance(source, str) or not source.strip():
            raise ValueError(f"missing source identity: {relative}")
        if member_set.memory is not None and member_set.memory.frontmatter.get("source-identity") != source:
            raise ValueError(f"{retained}: source-identity does not match review")
        if source in identities:
            raise ValueError(
                f"multiple selected reviews of source {source}; choose one boundary explicitly"
            )
        identities.add(source)
        memory = member_set.memory
        assert memory is not None  # a complete manifest names the memory member
        # The memory member's own validation above already accepted this
        # profile; reading it the same way keeps loading equal to publishing.
        profile = memory_member_comparison(memory.frontmatter, memory.body)
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
        raise ValueError("no generated main reviews selected")
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
