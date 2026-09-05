"""Read memory comparisons directly from retained main-analysis results."""

from __future__ import annotations

import csv
import io
import json
import re
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

from commonplace.lib.note_parser import parse_document

RESULT_TYPE = "kb/types/agentic-system-analysis-result.md"
RETAINED_ROOT = Path("kb/reports/retained/agentic-system-analysis")
REVIEWS_ROOT = Path("kb/agentic-systems/reviews")
RUN_ID = re.compile(r"AAS-\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*-\d{2}")
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
ASSESSMENTS = {"known", "absent", "inapplicable", "uninspected", "not-determinable"}
BASES = {"claimed", "afforded", "wired", "observed", "causally supported"}
METADATA = [
    "system_name",
    "review_file",
    "review_sha256",
    "result_file",
    "result_sha256",
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
    for suffix in ("", "_assessment", "_basis", "_records")
]


def retained_result_path(run_id: str) -> Path:
    if not isinstance(run_id, str) or not RUN_ID.fullmatch(run_id):
        raise ValueError("invalid analysis run ID")
    return RETAINED_ROOT / run_id / "result.md"


def _strings(value: object, label: str) -> list[str]:
    if not isinstance(value, list) or any(
        not isinstance(v, str) or not v.strip() for v in value
    ):
        raise ValueError(f"{label}: expected a list of nonempty strings")
    if len(value) != len(set(value)):
        raise ValueError(f"{label}: duplicate values")
    return value


def validate_comparison(profile: object, body: str) -> dict:
    """Validate authored assessments and references, without classifying prose."""
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
    shared = (
        body.split("## Shared records\n", 1)[1].split("## Runtime account", 1)[0]
        if "## Shared records\n" in body
        else ""
    )
    ids = set(
        re.findall(
            r"(?m)^\s*(?:\|\s*|[-*]\s+|#{3,6}\s+)?[*`]*((?:CMP|OBJ|RTE|CLM|ABS|BAP)-\d+)\b",
            shared,
        )
    )
    for name, vocabulary in AXES.items():
        entry = axes[name]
        if not isinstance(entry, dict) or set(entry) != {
            "assessment",
            "basis",
            "values",
            "records",
            "note",
        }:
            raise ValueError(
                f"{name}: requires assessment, basis, values, records, and note"
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
            raise ValueError(f"{name}: unresolved canonical records")
        if not set(values) <= vocabulary:
            raise ValueError(f"{name}: off-vocabulary values")
        if entry["assessment"] == "known":
            if (
                not values
                or not records
                or not isinstance(entry["basis"], str)
                or entry["basis"] not in BASES
            ):
                raise ValueError(
                    f"{name}: known assessment needs values, records, and evidence basis"
                )
        elif values or entry["basis"] is not None:
            raise ValueError(
                f"{name}: non-known assessment requires empty values and null basis"
            )
        if entry["assessment"] == "absent" and not any(
            r.startswith("ABS-") for r in records
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
    if faithfulness["values"] == ["yes"] and faithfulness["basis"] not in {
        "observed",
        "causally supported",
    }:
        raise ValueError("faithfulness_tested: yes requires execution evidence")
    return profile


def _document(content: bytes, label: str):
    document, error = parse_document(content.decode("utf-8"))
    if error or document is None or document.frontmatter is None:
        raise ValueError(f"{label}: malformed typed Markdown")
    return document


@dataclass(frozen=True)
class MatrixInputs:
    rows: list[dict[str, str]]
    hashes: dict[str, str]

    def recheck(self, root: Path) -> None:
        for path, digest in self.hashes.items():
            if sha256((root / path).read_bytes()).hexdigest() != digest:
                raise ValueError(f"input changed: {path}")


def load_results(root: Path, review_paths: list[Path] | None = None) -> MatrixInputs:
    """Select explicit main reviews, or all generated main reviews; fail on gaps."""
    root = root.resolve()
    paths = (
        review_paths
        if review_paths is not None
        else sorted((root / REVIEWS_ROOT).glob("*.md"))
    )
    rows, hashes, identities = [], {}, set()
    for raw_path in paths:
        path = (root / raw_path).resolve()
        relative = path.relative_to(root)
        if relative.parent != REVIEWS_ROOT or relative.suffix != ".md":
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
        retained = retained_result_path(meta.get("analysis-run"))
        if meta.get("analysis-result") != retained.as_posix():
            raise ValueError(
                f"{relative}: missing or mismatched retained result; regenerate the main review"
            )
        result_path = (root / retained).resolve()
        if result_path.relative_to(root) != retained:
            raise ValueError(f"retained result must use its canonical path: {retained}")
        result_bytes = result_path.read_bytes()
        result_hash = sha256(result_bytes).hexdigest()
        if meta.get("analysis-result-sha256") != result_hash:
            raise ValueError(f"retained result SHA-256 mismatch: {retained}")
        result = _document(result_bytes, str(retained))
        from commonplace.lib import validation

        checks = validation.validate_note(result_path, repo_root=root)
        if checks.fails or checks.warns:
            raise ValueError(
                f"invalid retained result {retained}: "
                + "; ".join([*checks.fails, *checks.warns])
            )
        data = result.frontmatter
        if (
            data.get("type") != RESULT_TYPE
            or data.get("result-disposition") != "complete"
        ):
            raise ValueError(f"not a complete main-analysis result: {retained}")
        if data.get("run-id") != meta["analysis-run"] or data.get(
            "reviewed-boundary"
        ) != meta.get("reviewed-revision"):
            raise ValueError(f"review/result identity mismatch: {relative}")
        source = meta.get("source-identity")
        if not isinstance(source, str) or not source.strip():
            raise ValueError(f"missing source identity: {relative}")
        register = result.body.split("## Source register\n", 1)[-1].split(
            "## Shared records", 1
        )[0]
        source_ids = {
            s.rstrip(".,;") for s in re.findall(r"https?://[^\s<>()`\"']+", register)
        }
        source_ids.update(re.findall(r"`([^`\n]+)`", register))
        if source not in source_ids:
            raise ValueError(
                f"source identity missing from result register: {relative}"
            )
        if source in identities:
            raise ValueError(
                f"multiple selected reviews of source {source}; choose one boundary explicitly"
            )
        identities.add(source)
        profile = validate_comparison(data.get("memory-comparison"), result.body)
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
                    result_hash,
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
            row[name] = json.dumps(sorted(entry["values"]), separators=(",", ":"))
            row[name + "_assessment"] = entry["assessment"]
            row[name + "_basis"] = entry["basis"] or ""
            row[name + "_records"] = ";".join(entry["records"])
        rows.append(row)
        hashes[relative.as_posix()] = row["review_sha256"]
        hashes[retained.as_posix()] = result_hash
    if not rows:
        raise ValueError("no generated main reviews selected")
    return MatrixInputs(
        sorted(
            rows, key=lambda row: (row["system_name"].casefold(), row["analysis_run"])
        ),
        hashes,
    )


def csv_text(inputs: MatrixInputs) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(inputs.rows)
    return output.getvalue()
