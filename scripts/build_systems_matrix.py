#!/usr/bin/env python3
"""Generate the wide comparison matrix (systems.csv) by parsing the reviews.

One row per code-backed review file in kb/agent-memory-systems/reviews/
(source_tier `code-grounded`, read from each review's `source-tier` frontmatter),
keyed by `review_file`. Doc-grounded reviews under lightweight/ are intentionally
excluded from this code-based matrix. The parsing logic
lives in the package library `commonplace.lib.systems_matrix` (text-in, row-out,
unit-tested); this runner owns file discovery, the legacy identity join
(public_repo / clone_path), and CSV writing. Hand-classified columns are
preserved across runs by review_file. Off-vocabulary and missing lead tokens are
reported, not guessed.

Output: kb/agent-memory-systems/systems.csv. Run:  python3 scripts/build_systems_matrix.py
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

from commonplace.lib.systems_matrix import (
    COLUMNS, JOINED, PARSED, norm, parse_review_text,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
AMS = REPO_ROOT / "kb" / "agent-memory-systems"
REVIEWS_DIR = AMS / "reviews"
SYSTEMS_CSV = AMS / "systems.csv"


def parse_review(path: Path, source_tier: str) -> tuple[dict[str, str], list[str]]:
    review_file = str(path.relative_to(REPO_ROOT))
    return parse_review_text(path.read_text(encoding="utf-8"), review_file, source_tier)


def read_source_tier(path: Path, default: str = "code-grounded") -> str:
    """Read the `source-tier` frontmatter value; default until Phase 1 backfills it."""
    m = re.search(r"^source-tier:\s*(\S+)", path.read_text(encoding="utf-8"), re.MULTILINE)
    return m.group(1).strip() if m else default


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
    for p in sorted(REVIEWS_DIR.glob("*.md")):
        if ".replaced." in p.name or p.name in ("dir-index.md", "README.md"):
            continue
        review_files.append((p, read_source_tier(p)))

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
        w = csv.DictWriter(fh, fieldnames=COLUMNS, extrasaction="ignore", lineterminator="\n")
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
