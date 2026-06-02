#!/usr/bin/env python3
"""Generate the wide comparison matrix (systems.csv) by parsing the reviews.

One row per review file in kb/agent-memory-systems/reviews/ (source_tier
`repo-reviewed`) and kb/agent-memory-systems/lightweight/ (source_tier
`lightweight`), keyed by `review_file`. Columns are every candidate axis from
comparison-feature-dictionary.md.

Parsed from each review:
  - system_name            <- the H1 title
  - storage_substrate      <- body lead token  **Storage substrate:** `...`
  - representational_form  <- body lead token  **Representational form:** `...`
  - read_back_direction    <- body lead token  **Read-back:** `...`
  - read_back_notes        <- the justification trailing the read-back token
  - trace_derived          <- `trace-derived` frontmatter tag (yes/no)
  - push_engineered        <- `push-activation` frontmatter tag (yes/no)
Joined from the legacy inventory (public_repo / clone_path) by normalised name
or repo/clone-path segment. Hand-classified columns (lineage, behavioral
authority, the trace-derived sub-axes, etc.) are preserved across runs by
review_file. Off-vocabulary tokens and missing tokens are reported, not guessed.

Output: kb/agent-memory-systems/systems.csv. Run:  python3 scripts/build_systems_matrix.py
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AMS = REPO_ROOT / "kb" / "agent-memory-systems"
REVIEWS_DIR = AMS / "reviews"
LIGHTWEIGHT_DIR = AMS / "lightweight"
SYSTEMS_CSV = AMS / "systems.csv"

COLUMNS = [
    "system_name", "review_file", "public_repo", "clone_path",
    "one_line", "source_tier", "maturity", "integration_surface",
    "storage_substrate", "representational_form", "lineage_origin",
    "lineage_status", "behavioral_authority",
    "trace_derived", "trace_source", "extraction_trigger",
    "distillation_oracle", "distilled_form", "learning_scope", "learning_timing",
    "read_back_direction", "push_engineered", "read_back_trigger",
    "read_back_timing", "read_back_authority", "faithfulness_tested", "read_back_notes",
    "link_model", "access_mode",
    "temporal_model", "curation_ops",
    "context_strategy",
    "env_fit", "api_lock_in", "degrades_to_files",
    "agency_model",
]

# Columns the parser owns (recomputed from the review every run). Everything
# else is hand-classified and preserved across runs.
PARSED = {
    "system_name", "review_file", "source_tier",
    "storage_substrate", "representational_form",
    "read_back_direction", "read_back_notes",
    "trace_derived", "push_engineered",
}
JOINED = {"public_repo", "clone_path"}

VOCAB = {
    "storage_substrate": {"files", "repo", "sqlite", "rdbms", "vector", "graph",
                          "kv", "in-memory", "prompt-registry", "model-weights",
                          "service-object"},
    "representational_form": {"prose", "symbolic", "parametric", "mixed"},
    "read_back_direction": {"pull", "push", "both"},
}

_H1 = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
_TAGS = re.compile(r"^tags:\s*\[([^\]]*)\]", re.MULTILINE)


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def _token(label: str, text: str) -> str:
    m = re.search(rf"\*\*{re.escape(label)}:\*\*\s*`([^`]+)`", text)
    return m.group(1).strip() if m else ""


def parse_review(path: Path, source_tier: str) -> tuple[dict[str, str], list[str]]:
    """Extract the parsed fields from one review file. Returns (row, flags)."""
    text = path.read_text(encoding="utf-8")
    flags: list[str] = []
    row = {c: "" for c in COLUMNS}
    row["review_file"] = str(path.relative_to(REPO_ROOT))
    row["source_tier"] = source_tier

    h1 = _H1.search(text)
    row["system_name"] = h1.group(1).strip() if h1 else path.stem

    tags = set()
    mt = _TAGS.search(text)
    if mt:
        tags = {t.strip() for t in mt.group(1).split(",") if t.strip()}
    row["trace_derived"] = "yes" if "trace-derived" in tags else "no"
    row["push_engineered"] = "yes" if "push-activation" in tags else "no"

    row["storage_substrate"] = _token("Storage substrate", text)
    row["representational_form"] = _token("Representational form", text)
    row["read_back_direction"] = _token("Read-back", text)

    # read-back justification: text after the token up to end of line
    mrb = re.search(r"\*\*Read-back:\*\*\s*`[^`]+`\s*[—-]+\s*(.+)", text)
    if mrb:
        row["read_back_notes"] = mrb.group(1).strip()

    # validate / flag
    for col in ("storage_substrate", "representational_form", "read_back_direction"):
        v = row[col]
        if not v:
            flags.append(f"{col}: missing")
        elif v not in VOCAB[col]:
            flags.append(f"{col}: off-vocab `{v}`")
    return row, flags


def load_inventory() -> list[dict[str, str]]:
    """Legacy systems.csv rows, for the public_repo / clone_path join."""
    if not SYSTEMS_CSV.exists():
        return []
    legacy = {"system name": "system_name", "public repo": "public_repo",
              "path to cloned repo": "clone_path"}
    with SYSTEMS_CSV.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    out = []
    for r in rows:
        out.append({legacy.get(k, k): (v or "").strip() for k, v in r.items()})
    return out


def main() -> int:
    if not REVIEWS_DIR.is_dir():
        print(f"missing {REVIEWS_DIR}", file=sys.stderr)
        return 1

    inventory = load_inventory()
    # identity index: any of {norm name, repo last-seg, clonepath last-seg} -> (repo, clonepath)
    def lastseg(u: str) -> str:
        return norm(re.sub(r"[#?].*$", "", u.rstrip("/")).split("/")[-1]) if u else ""
    ident: dict[str, tuple[str, str]] = {}
    for r in inventory:
        for k in {norm(r.get("system_name", "")), lastseg(r.get("public_repo", "")),
                  lastseg(r.get("clone_path", ""))}:
            if k and k not in ident:
                ident[k] = (r.get("public_repo", ""), r.get("clone_path", ""))
    # prior hand-classified values, keyed by review_file
    prior = {r["review_file"]: r for r in inventory if r.get("review_file")}

    review_files = []
    for d, tier in ((REVIEWS_DIR, "repo-reviewed"), (LIGHTWEIGHT_DIR, "lightweight")):
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            if ".replaced." in p.name or p.name in ("dir-index.md", "README.md"):
                continue
            review_files.append((p, tier))

    rows: list[dict[str, str]] = []
    all_flags: list[tuple[str, str]] = []
    joined = 0
    for path, tier in review_files:
        row, flags = parse_review(path, tier)
        # preserve hand-classified columns from a prior run
        old = prior.get(row["review_file"])
        if old:
            for c in COLUMNS:
                if c not in PARSED and c not in JOINED and old.get(c):
                    row[c] = old[c]
        # join identity
        key = norm(path.stem)
        if key in ident:
            row["public_repo"], row["clone_path"] = ident[key]
            joined += 1
        rows.append(row)
        for f in flags:
            all_flags.append((row["review_file"], f))

    rows.sort(key=lambda r: (r["source_tier"], r["system_name"].lower()))
    with SYSTEMS_CSV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    tiers = {}
    for r in rows:
        tiers[r["source_tier"]] = tiers.get(r["source_tier"], 0) + 1
    print(f"rows written: {len(rows)}  ({', '.join(f'{k}={v}' for k, v in sorted(tiers.items()))})")
    print(f"identity (repo/clone) joined: {joined}/{len(rows)}")
    print(f"flags: {len(all_flags)}")
    for rf, f in all_flags:
        print(f"  - {Path(rf).name}: {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
