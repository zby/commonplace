"""Read memory comparisons directly from retained analysis artifacts."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Mapping
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

from commonplace.lib.agentic_analysis.analyses import analysis_layout, current_analyses
from commonplace.lib.agentic_analysis.records import (
    declared_ids,
    identifier_from_anchor,
    is_absence,
)

__all__ = [
    "AXES",
    "csv_text",
    "load_results",
    "profile_member_comparison",
    "project_comparison",
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
    "comparison_version",
    "one_line",
]
COLUMNS = METADATA + [
    name + suffix
    for name in AXES
    for suffix in ("", "_assessment", "_evidence", "_records", "_units", "_note")
]


def _strings(value: object, label: str) -> list[str]:
    if not isinstance(value, list) or any(
        not isinstance(v, str) or not v.strip() for v in value
    ):
        raise ValueError(f"{label}: expected a list of nonempty strings")
    if len(value) != len(set(value)):
        raise ValueError(f"{label}: duplicate values")
    return value


def _validate_applicability(row: dict) -> None:
    """Whole-axis inapplicability needs complete coverage of its prerequisite."""
    trace_negative = (
        row["trace_learning_assessment"] == "absent"
        or (row["trace_learning_assessment"] == "known" and row["trace_learning"] == ["no"])
    )
    if row["trace_source_assessment"] == "inapplicable" and not trace_negative:
        raise ValueError("trace_source: inapplicability requires complete bounded trace-learning absence")
    direction_negative = (
        row["read_back_direction_assessment"] == "absent"
        or (row["read_back_direction_assessment"] == "known" and row["read_back_direction"] == ["pull"])
    )
    # Bounded absent read-back has no push selector, just as complete pull-only
    # read-back does. Unresolved or push-containing inventories do not qualify.
    if row["read_back_signal_assessment"] == "inapplicable" and not direction_negative:
        raise ValueError("read_back_signal: inapplicability requires complete pull-only or bounded absent read-back")


def _refs(value: object, label: str, ids: Mapping[str, str], *, required: bool = False) -> list[str]:
    """The record IDs a list of citations names, each `member.md#anchor` declared by that member.

    ``ids`` maps each record ID the profile may cite to the member declaring it.
    """
    cited = []
    for ref in _strings(value, label):
        member, separator, fragment = ref.partition("#")
        identifier = identifier_from_anchor(fragment)
        if not separator or identifier is None or not member or "/" in member:
            raise ValueError(f"{label}: invalid record citation {ref!r}; use member.md#record-anchor")
        if ids.get(identifier) != member:
            raise ValueError(f"{label}: unresolved records")
        cited.append(identifier)
    if required and not cited:
        raise ValueError(f"{label}: unresolved records")
    return cited


def _coverage(entry: dict, label: str, ids: Mapping[str, str]) -> None:
    if not isinstance(entry["assessment"], str) or entry["assessment"] not in ASSESSMENTS:
        raise ValueError(f"{label}: invalid assessment")
    if not isinstance(entry["note"], str) or not entry["note"].strip():
        raise ValueError(f"{label}: missing rationale or conclusion prevented")
    refs = _refs(entry["records"], label + ".records", ids, required=entry["assessment"] in {
        "known", "partial", "absent", "inapplicable",
    })
    if entry["assessment"] == "absent" and not any(is_absence(ref) for ref in refs):
        raise ValueError(f"{label}: absence requires an evidenced-absence record")


def validate_comparison(profile: object, *, known_ids: Mapping[str, str]) -> dict:
    """Check structure and canonical references, not the truth of source claims."""
    if not isinstance(profile, dict) or set(profile) != {"version", "scope", "axes"}:
        raise ValueError("memory-comparison requires version, scope and axes")
    if type(profile["version"]) is not int or profile["version"] != 2:
        raise ValueError("memory-comparison: unsupported version")
    if not isinstance(profile["scope"], str) or not profile["scope"].strip():
        raise ValueError("memory-comparison.scope must name the compared memory boundary")
    axes = profile["axes"]
    if not isinstance(axes, dict) or set(axes) != set(AXES):
        raise ValueError("memory-comparison.axes must contain every registered axis exactly once")
    resolved = {"known", "absent", "inapplicable"}
    for name, vocabulary in AXES.items():
        entry = axes[name]
        if not isinstance(entry, dict) or set(entry) != {"assessment", "units", "records", "note"}:
            raise ValueError(f"{name}: requires assessment, units, records, and note")
        _coverage(entry, name, known_ids)
        units = entry["units"]
        if not isinstance(units, list):
            raise ValueError(f"{name}: units must be a list")  # noqa: TRY004 - validation API
        positives = []
        for index, unit in enumerate(units):
            label = f"{name}.units[{index}]"
            if not isinstance(unit, dict) or set(unit) != {"scope", "assessment", "findings", "records", "note"}:
                raise ValueError(f"{label}: requires scope, assessment, findings, records, and note")
            if not isinstance(unit["scope"], str) or not unit["scope"].strip():
                raise ValueError(f"{label}: missing unit scope")
            _coverage(unit, label, known_ids)
            findings = unit["findings"]
            if not isinstance(findings, list):
                raise ValueError(f"{label}: findings must be a list")  # noqa: TRY004 - validation API
            for finding in findings:
                if not isinstance(finding, dict) or set(finding) != {"value", "basis", "records", "note"}:
                    raise ValueError(f"{label}: finding requires value, basis, records, and note")
                if not isinstance(finding["value"], str) or finding["value"] not in vocabulary:
                    raise ValueError(f"{label}: off-vocabulary value")
                if not isinstance(finding["basis"], str) or finding["basis"] not in BASES:
                    raise ValueError(f"{label}: invalid evidence basis")
                refs = _refs(finding["records"], label + ".finding.records", known_ids, required=True)
                if not isinstance(finding["note"], str) or not finding["note"].strip():
                    raise ValueError(f"{label}: missing evidence rationale")
                if name == "trace_learning" and finding["value"] == "no":
                    if unit["assessment"] != "known" or not any(is_absence(ref) for ref in refs):
                        raise ValueError(f"{label}: local no requires resolved bounded absence")
                else:
                    positives.append(finding)
            if unit["assessment"] in {"known", "partial"}:
                if not findings:
                    raise ValueError(f"{label}: positive assessment needs findings")
            elif findings:
                raise ValueError(f"{label}: non-positive assessment requires empty findings")
            if name == "trace_learning" and {f["value"] for f in findings} == {"yes", "no"}:
                raise ValueError(f"{label}: yes and no require distinct units")
        status = entry["assessment"]
        unresolved = any(unit["assessment"] not in resolved for unit in units)
        if status == "known" and (not units or unresolved):
            raise ValueError(f"{name}: known coverage requires resolved units")
        if status == "known" and all(unit["assessment"] == "inapplicable" for unit in units):
            raise ValueError(f"{name}: wholly inapplicable units require inapplicable axis coverage")
        if status == "partial" and (not positives or not unresolved):
            raise ValueError(f"{name}: partial coverage needs positives and unresolved coverage")
        if status not in {"known", "partial"} and positives:
            raise ValueError(f"{name}: non-positive assessment requires empty positive findings")
        if status in {"absent", "inapplicable"} and any(unit["findings"] for unit in units):
            raise ValueError(f"{name}: absence or inapplicability requires empty findings")
        if status in {"absent", "inapplicable"} and any(unit["assessment"] != status for unit in units):
            raise ValueError(f"{name}: incompatible unit coverage")
    projected = project_comparison(profile)
    _validate_applicability(projected)
    if (
        projected["trace_learning_assessment"] == "known"
        and projected["trace_learning"] == ["no"]
        and axes["trace_source"]["assessment"] != "inapplicable"
    ):
        raise ValueError("trace_source: must be inapplicable when trace learning is no")
    if (
        projected["read_back_direction_assessment"] == "known"
        and projected["read_back_direction"] == ["pull"]
        and axes["read_back_signal"]["assessment"] != "inapplicable"
    ):
        raise ValueError("read_back_signal: must be inapplicable for pull-only read-back")
    return profile


def _cited_ids(citations: list[str]) -> list[str]:
    """Record IDs for a revision-2 citation list; the matrix reports records by ID."""
    return [identifier_from_anchor(citation.partition("#")[2]) or citation for citation in citations]


def project_comparison(profile: dict) -> dict:
    """Derive unions and strongest existence witnesses; retain local evidence."""
    row = {"comparison_version": profile["version"]}
    ranks = {basis: index for index, basis in enumerate(
        ("claimed", "afforded", "wired", "observed", "causally supported")
    )}
    for name, entry in profile["axes"].items():
        units = entry["units"]
        evidence = {}
        for unit in units:
            for finding in unit["findings"]:
                value = finding["value"]
                if value not in evidence or ranks[finding["basis"]] > ranks[evidence[value]["basis"]]:
                    evidence[value] = {"basis": finding["basis"], "records": _cited_ids(finding["records"]),
                                       "note": finding["note"]}
        if name == "trace_learning" and ("yes" in evidence or entry["assessment"] != "known"):
            evidence.pop("no", None)
        row[name] = sorted(evidence)
        row[name + "_assessment"] = entry["assessment"]
        row[name + "_evidence"] = evidence
        row[name + "_records"] = _cited_ids(entry["records"])
        row[name + "_units"] = units
        row[name + "_note"] = entry["note"]
    return row


def profile_member_comparison(metadata: dict, *, record_bodies: dict[str, str]) -> dict:
    """Resolve profile support against the records the given members declare.

    The artifact rule checks the record members themselves.
    """
    known = {identifier: name for name, body in record_bodies.items() for identifier in declared_ids(body)}
    return validate_comparison(metadata.get("memory-comparison"), known_ids=known)


@dataclass(frozen=True)
class MatrixInputs:
    rows: list[dict]
    hashes: dict[str, str]


def load_results(root: Path, review_paths: list[Path] | None = None) -> MatrixInputs:
    """Select explicit current overviews, or all current analyses; fail on gaps.

    The shared enumerator validates membership and manifest hashes. Identity
    comes from the overview and comparison data from the profile member.
    """
    from commonplace.lib.validation import ValidationRun

    root = root.resolve()
    run = ValidationRun(root, ())
    analyses = current_analyses(root, run=run)
    layout = analysis_layout()
    selected = None if review_paths is None else {(root / path).resolve() for path in review_paths}
    available = {analysis.overview.path for analysis in analyses}
    if selected is not None and not selected <= available:
        raise ValueError("selected path is not a current analysis overview")
    rows, hashes = [], {}
    for analysis in analyses:
        path = analysis.overview.path
        if selected is not None and path not in selected:
            continue
        relative = path.relative_to(root)
        review_bytes = analysis.overview.content
        manifest_path = analysis.artifact.path / "ARTIFACT.yaml"
        retained = manifest_path.relative_to(root)
        manifest_hash = sha256(analysis.artifact.content).hexdigest()
        data = analysis.overview.frontmatter
        source = analysis.memory.frontmatter["source-identity"]
        meta = {**data, "analysis-run": data["run-id"]}
        member = analysis.memory_profile
        assert member is not None  # complete analyses require the separate profile
        cited = layout.roles["memory-profile"].cites
        profile = profile_member_comparison(member.frontmatter, record_bodies={
            layout.path(role): analysis.roles[role].body for role in cited if role in analysis.roles
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
                    profile["version"],
                    str(meta.get("description", "")),
                ],
            )
        )
        row.update(project_comparison(profile))
        rows.append(row)
        hashes[relative.as_posix()] = row["review_sha256"]
        hashes[retained.as_posix()] = manifest_hash
        for document in analysis.documents:
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
    if row[axis + "_assessment"] == "inapplicable":
        return None
    units = row[axis + "_units"]
    if not units or all(unit["assessment"] == "inapplicable" for unit in units):
        return None
    if any(
        unit["assessment"] not in {"known", "absent", "inapplicable"}
        or any(finding["basis"] not in STRONG_BASES for finding in unit["findings"])
        for unit in units
    ):
        return None
    values = set(row[axis])
    if row[axis + "_assessment"] == "known" and values == supported_values(row, axis):
        return tuple(sorted(values))
    return None


def csv_row(row: dict) -> dict[str, str]:
    """Serialize one structured row; JSON cells exist only in the CSV file."""
    out = {name: str(row[name]) for name in METADATA}
    for axis in AXES:
        out[axis] = json.dumps(row[axis], separators=(",", ":"))
        out[axis + "_assessment"] = row[axis + "_assessment"]
        out[axis + "_note"] = row[axis + "_note"]
        out[axis + "_evidence"] = json.dumps(
            row[axis + "_evidence"], sort_keys=True, separators=(",", ":")
        )
        out[axis + "_records"] = ";".join(row[axis + "_records"])
        out[axis + "_units"] = json.dumps(
            row[axis + "_units"], sort_keys=True, separators=(",", ":")
        )
    return out


def csv_text(inputs: MatrixInputs) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(csv_row(row) for row in inputs.rows)
    return output.getvalue()
