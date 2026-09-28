"""Read memory comparisons directly from retained analysis sets."""

from __future__ import annotations

import csv
import functools
import io
import json
import re
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

import yaml

from commonplace.lib.agentic_records import section
from commonplace.lib.agentic_set import (
    OVERVIEW_TYPE,
    RETAINED_ROOT,
    RUN_ID,
    load_member_set,
    retained_overview_path,
)
from commonplace.lib.note_parser import parse_document

__all__ = [
    "AXES",
    "RETAINED_ROOT",
    "RUN_ID",
    "csv_text",
    "load_results",
    "retained_overview_path",
    "shared_record_ids",
    "validate_comparison",
]
REVIEWS_ROOT = Path("kb/agentic-systems/reviews")
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
    "overview_file",
    "overview_sha256",
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


def shared_record_ids(body: str, *, memory_report: bool = False) -> set[str]:
    """IDs declared at line start under Shared records; proposals count in a local report."""
    shared = section(body, "Shared records")
    record_prefix = r"(?:MEM-)?" if memory_report else ""
    return set(
        re.findall(
            rf"(?m)^\s*(?:\|\s*|[-*]\s+|#{{3,6}}\s+)?[*`]*({record_prefix}(?:CMP|OBJ|RTE|CLM|ABS|BAP)-\d+)\b",
            shared,
        )
    )


def validate_comparison(
    profile: object,
    body: str,
    *,
    memory_report: bool = False,
    known_ids: set[str] | None = None,
) -> dict:
    """Validate authored assessments and references, without classifying prose.

    ``known_ids`` replaces the IDs parsed from the body's Shared records: a
    finalized memory member cites records other members declare, and a set
    verifier supplies the whole set's declarations.
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
    ids = known_ids if known_ids is not None else shared_record_ids(
        body, memory_report=memory_report
    )
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


@dataclass(frozen=True)
class MatrixInputs:
    rows: list[dict[str, str]]
    hashes: dict[str, str]

    def recheck(self, root: Path) -> None:
        for path, digest in self.hashes.items():
            if sha256((root / path).read_bytes()).hexdigest() != digest:
                raise ValueError(f"input changed: {path}")


_MISSING_LINK = re.compile(r"link health: missing target (?P<link>\S+)$")


@functools.cache
def _redirect_sources(root: Path) -> frozenset[Path]:
    """Paths the published site redirects, as files under its docs_dir."""
    config_path = root / "properdocs.yml"
    if not config_path.is_file():
        return frozenset()
    config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    docs_dir = (root / str(config.get("docs_dir", "kb"))).resolve()
    maps = next(
        (
            plugin["redirects"].get("redirect_maps") or {}
            for plugin in config.get("plugins") or []
            if isinstance(plugin, dict) and isinstance(plugin.get("redirects"), dict)
        ),
        {},
    )
    return frozenset((docs_dir / old).resolve() for old in maps if isinstance(old, str))


def _redirected_link(warning: str, source: Path, root: Path) -> bool:
    match = _MISSING_LINK.search(warning)
    if match is None:
        return False
    target = (source.parent / match.group("link").split("#", 1)[0]).resolve()
    return target in _redirect_sources(root.resolve())


def _validated_overview(root: Path, path: Path, label: str) -> None:
    """Validate the retained overview; its set rule covers every member."""
    from commonplace.lib import validation

    checks = validation.validate_note(path, repo_root=root)
    # Retained members keep their link bytes; a link to a retired artifact
    # resolves through the published redirect map instead.
    warns = [warn for warn in checks.warns if not _redirected_link(warn, path, root)]
    if checks.fails or warns:
        raise ValueError(f"invalid retained {label}: " + "; ".join([*checks.fails, *warns]))


def load_results(root: Path, review_paths: list[Path] | None = None) -> MatrixInputs:
    """Select explicit main reviews, or all generated main reviews; fail on gaps.

    Each review pins its run's retained overview. Validating the overview
    checks the whole set; the loader then takes identity and the register
    from the overview and the profile from the memory member.
    """
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
        retained = retained_overview_path(meta.get("analysis-run"))
        if meta.get("analysis-overview") != retained.as_posix():
            raise ValueError(
                f"{relative}: missing or mismatched retained overview; regenerate the main review"
            )
        overview_path = (root / retained).resolve()
        if overview_path.relative_to(root) != retained:
            raise ValueError(f"retained overview must use its canonical path: {retained}")
        overview_hash = sha256(overview_path.read_bytes()).hexdigest()
        if meta.get("analysis-overview-sha256") != overview_hash:
            raise ValueError(f"retained overview SHA-256 mismatch: {retained}")
        _validated_overview(root, overview_path, str(retained))
        member_set = load_member_set(overview_path)
        data = member_set.overview.frontmatter
        if (
            data.get("type") != OVERVIEW_TYPE
            or data.get("result-disposition") != "complete"
        ):
            raise ValueError(f"not a complete analysis overview: {retained}")
        if data.get("run-id") != meta["analysis-run"] or data.get(
            "reviewed-boundary"
        ) != meta.get("reviewed-revision"):
            raise ValueError(f"review/overview identity mismatch: {relative}")
        source = meta.get("source-identity")
        if not isinstance(source, str) or not source.strip():
            raise ValueError(f"missing source identity: {relative}")
        register = section(member_set.overview.body, "Source register")
        source_ids = {
            s.rstrip(".,;") for s in re.findall(r"https?://[^\s<>()`\"']+", register)
        }
        source_ids.update(re.findall(r"`([^`\n]+)`", register))
        if source not in source_ids:
            raise ValueError(
                f"source identity missing from overview register: {relative}"
            )
        if source in identities:
            raise ValueError(
                f"multiple selected reviews of source {source}; choose one boundary explicitly"
            )
        identities.add(source)
        memory = member_set.memory
        assert memory is not None  # a complete manifest names the memory member
        profile = memory.frontmatter["memory-comparison"]
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
                    overview_hash,
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
            row[name + "_evidence"] = json.dumps(
                entry["evidence"], sort_keys=True, separators=(",", ":")
            )
            row[name + "_records"] = ";".join(entry["records"])
        rows.append(row)
        hashes[relative.as_posix()] = row["review_sha256"]
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


def supported_values(row: dict[str, str], axis: str) -> set[str]:
    """Positive implementation evidence, counted once per value and system."""
    if row["source_tier"] != "code-grounded":
        return set()
    return {
        value
        for value, support in json.loads(row[axis + "_evidence"]).items()
        if support["basis"] in STRONG_BASES
    }


def complete_values(row: dict[str, str], axis: str) -> str:
    """Complete strong profiles only; a filtered subset is not a full profile."""
    if row["source_tier"] != "code-grounded":
        return ""
    if row[axis + "_assessment"] == "absent":
        return "none"
    values = set(json.loads(row[axis]))
    if row[axis + "_assessment"] == "known" and values == supported_values(row, axis):
        return json.dumps(sorted(values), separators=(",", ":"))
    return ""


def csv_text(inputs: MatrixInputs) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(inputs.rows)
    return output.getvalue()
