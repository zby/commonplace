#!/usr/bin/env python3
"""Extract link-relationship labels from KB footer annotations.

Walks kb/**/*.md, matches lines shaped like:
    - [text](path.md) — <label>[:/] ...
Classifies source + target by collection, buckets labels per edge,
and writes a markdown report to kb/reports/link-vocabulary.md.

Throwaway — rerun to refresh.
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
KB = REPO / "kb"

COLLECTION_REGISTER = {
    "notes": "theoretical",
    "reference": "descriptive",
    "instructions": "prescriptive",
    "agent-memory-systems": "descriptive",
    "work": "workshop",
    "sources": "source",
    "reports": "managed",
    "tasks": "other",
    "types": "schema",
}

ADR_009 = {
    "extends",
    "grounds", "foundation",
    "contradicts",
    "enables",
    "exemplifies", "example",
}

# Labels declared in kb/reports/collection-topology.md.
# Prose connectors like since/because are inline grammar, but the
# matrix lists them in the outbound tables so we count them here too.
MATRIX_LABELS = {
    ("theoretical", "theoretical"): {"since", "because", "contradicts", "extends", "qualifies"},
    ("theoretical", "descriptive"): {"evidence", "derived-from", "exemplifies"},
    ("theoretical", "prescriptive"): {"evidence"},
    ("descriptive", "descriptive"): {"cross-reference", "see-also", "supersedes"},
    ("descriptive", "theoretical"): {"rationale", "grounds", "evidence"},
    ("descriptive", "prescriptive"): {"procedure"},
    ("prescriptive", "theoretical"): {"justification"},
    ("prescriptive", "descriptive"): {"reference"},
    ("prescriptive", "prescriptive"): {"composition"},
}

LINK_RE = re.compile(
    r"""^\s*[-*]\s*
    \[([^\]]+)\]
    \(([^)]+\.md)\)
    \s*(?:—|--|&mdash;)\s*
    (.+?)\s*$
    """,
    re.VERBOSE,
)

PROSE_STARTERS = {"the", "a", "an", "this", "these", "those", "it", "its", "how", "what", "why", "when", "where"}


def source_register(path: Path) -> str:
    try:
        rel = path.relative_to(KB)
    except ValueError:
        return "other"
    top = rel.parts[0] if rel.parts else "other"
    return COLLECTION_REGISTER.get(top, "other")


def target_register(source_file: Path, target_path: str) -> str:
    if target_path.startswith(("http://", "https://", "#", "mailto:")):
        return "external"
    target = (source_file.parent / target_path).resolve()
    try:
        rel = target.relative_to(KB)
    except ValueError:
        return "external"
    top = rel.parts[0] if rel.parts else "other"
    return COLLECTION_REGISTER.get(top, "other")


def extract_labels(annotation: str) -> list[str]:
    ann = annotation.strip()
    ann = re.sub(r"^\*\*([^*]+)\*\*", r"\1", ann)
    m = re.match(r"^([a-zA-Z][\w\- /]*?)\s*:\s", ann)
    if not m:
        return []
    prefix = m.group(1).strip()
    if len(prefix) > 30 or len(prefix.split()) > 3:
        return []
    first = prefix.split()[0].lower()
    if first in PROSE_STARTERS:
        return []
    parts = []
    for p in prefix.split("/"):
        cleaned = re.sub(r"\s+", "-", p.strip().strip("*")).lower()
        if cleaned:
            parts.append(cleaned)
    return parts


def label_status(source_reg: str, target_reg: str, label: str) -> str:
    adr = label in ADR_009
    in_matrix = label in MATRIX_LABELS.get((source_reg, target_reg), set())
    if adr and in_matrix:
        return "adr+matrix"
    if adr:
        return "adr-only"
    if in_matrix:
        return "matrix-only"
    return "off-vocab"


def main() -> None:
    counts: dict[tuple[str, str, str], int] = defaultdict(int)
    examples: dict[tuple[str, str, str], list[str]] = defaultdict(list)
    totals_per_edge: Counter[tuple[str, str]] = Counter()
    annotated = 0
    unlabelled = 0

    for path in sorted(KB.rglob("*.md")):
        text = path.read_text(errors="replace")
        src_reg = source_register(path)
        for line in text.splitlines():
            m = LINK_RE.match(line)
            if not m:
                continue
            _text, target, annotation = m.groups()
            tgt_reg = target_register(path, target)
            labels = extract_labels(annotation)
            if not labels:
                unlabelled += 1
                labels = ["<unlabelled>"]
            else:
                annotated += 1
            for label in labels:
                key = (src_reg, tgt_reg, label)
                counts[key] += 1
                totals_per_edge[(src_reg, tgt_reg)] += 1
                if len(examples[key]) < 2:
                    try:
                        rel = path.relative_to(REPO)
                    except ValueError:
                        rel = path
                    examples[key].append(f"`{rel}` → `{target}`")

    out_lines = [
        "---",
        'description: "Machine-generated audit of link-relationship labels used across KB footer annotations. Rebuild with kb/work/link-label-audit/extract_labels.py."',
        "type: note",
        "status: current",
        "---",
        "",
        "# Link vocabulary audit",
        "",
        "Footer-annotation labels grouped by `(source register → target register)`. "
        f"ADR 009 vocabulary: `{', '.join(sorted(ADR_009))}`. "
        "Status column: `adr+matrix` (declared in both), `adr-only`, `matrix-only`, or `off-vocab`.",
        "",
        f"- Footer-shaped link lines matched: **{annotated + unlabelled}**",
        f"- With a label-shaped prefix: **{annotated}**",
        f"- Unlabelled (prose-only annotations): **{unlabelled}**",
        "",
    ]

    edges = sorted(totals_per_edge, key=lambda e: -totals_per_edge[e])
    for edge in edges:
        src, tgt = edge
        out_lines.append(f"## {src} → {tgt}  (n = {totals_per_edge[edge]})")
        out_lines.append("")
        declared = MATRIX_LABELS.get(edge, set())
        if declared:
            out_lines.append(f"Matrix vocabulary for this edge: `{', '.join(sorted(declared))}`")
        else:
            out_lines.append("_No declared matrix vocabulary for this edge._")
        out_lines.append("")
        out_lines.append("| Label | Count | Status | Example |")
        out_lines.append("|---|---|---|---|")
        edge_labels = sorted(
            ((label, counts[(src, tgt, label)]) for label in {k[2] for k in counts if (k[0], k[1]) == edge}),
            key=lambda x: (-x[1], x[0]),
        )
        for label, count in edge_labels:
            status = label_status(src, tgt, label)
            ex = examples[(src, tgt, label)][0] if examples[(src, tgt, label)] else ""
            out_lines.append(f"| `{label}` | {count} | {status} | {ex} |")
        out_lines.append("")

    out = KB / "reports" / "link-vocabulary.md"
    out.write_text("\n".join(out_lines) + "\n")
    print(f"Wrote {out}")
    print(f"Edges: {len(edges)}, labels: {len({k[2] for k in counts})}, total links: {sum(totals_per_edge.values())}")


if __name__ == "__main__":
    main()
