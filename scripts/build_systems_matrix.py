#!/usr/bin/env python3
"""Generate the wide comparison matrix (systems.csv) by parsing the reviews.

One row per code-backed review file in kb/agent-memory-systems/reviews/, keyed by
`review_file`. The `reviews/` location is authoritative for source_tier
(`code-grounded`); each review's `source-tier` frontmatter is validated against it
and missing/mismatched values are flagged, not trusted. Doc-grounded reviews under
lightweight/ are intentionally excluded from this code-based matrix. The parsing
logic lives in the package library `commonplace.lib.systems_matrix` (text-in,
row-out, unit-tested); this runner owns file discovery, the legacy identity join
(public_repo / clone_path), and CSV writing. Hand-classified columns are
preserved across runs by review_file. Off-vocabulary tokens, missing frontmatter,
and tier mismatches are reported, not guessed.

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
RELATED_SYSTEMS = REPO_ROOT / "related-systems"

# reviews/ is the code-grounded tier by location; this is authoritative for the
# written row. Each review's `source-tier` frontmatter is validated against it
# (missing or mismatched values are flagged), not trusted as the source of truth.
REVIEWS_TIER = "code-grounded"


def parse_review(path: Path, source_tier: str) -> tuple[dict[str, str], list[str]]:
    review_file = str(path.relative_to(REPO_ROOT))
    return parse_review_text(path.read_text(encoding="utf-8"), review_file, source_tier)


def read_review_identity(path: Path) -> tuple[str, str]:
    """Return explicit Repository / Source directory metadata from a review."""
    text = path.read_text(encoding="utf-8")

    def field(label: str) -> str:
        match = re.search(rf"^\*\*{re.escape(label)}:\*\*\s*(.+?)\s*$", text, re.MULTILINE)
        return match.group(1).strip() if match else ""

    return field("Repository"), field("Source directory")


def derive_clone_path(repo_url: str) -> str:
    """Infer a local checkout path from a GitHub repo URL when it exists."""
    clean = re.sub(r"[#?].*$", "", repo_url.strip().removesuffix(".git").rstrip("/"))
    match = re.search(r"github\.com/([^/]+)/([^/]+)$", clean)
    if not match:
        return ""
    owner, repo = match.groups()
    candidates = [
        RELATED_SYSTEMS / f"{owner}--{repo}",
        RELATED_SYSTEMS / repo,
    ]
    for candidate in candidates:
        if candidate.is_dir():
            return str(candidate.relative_to(REPO_ROOT))
    return ""


def read_source_tier(path: Path) -> str | None:
    """Read the `source-tier` frontmatter value, or None if absent (flagged in main)."""
    m = re.search(r"^source-tier:\s*(\S+)", path.read_text(encoding="utf-8"), re.MULTILINE)
    return m.group(1).strip() if m else None


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
        # Location is authoritative for the tier written; validate the declared
        # frontmatter against it and flag drift rather than trusting it blindly.
        row, flags = parse_review(path, REVIEWS_TIER)
        if tier is None:
            flags.append("source-tier: missing frontmatter")
        elif tier != REVIEWS_TIER:
            flags.append(
                f"source-tier: frontmatter says {tier!r}, expected {REVIEWS_TIER!r} for reviews/"
            )
        # preserve hand-classified columns from a prior run
        old = prior.get(row["review_file"])
        if old:
            for c in COLUMNS:
                if c not in PARSED and c not in JOINED and old.get(c):
                    row[c] = old[c]
        # join identity. Prefer explicit current-review metadata over the legacy
        # CSV inventory so renamed/colliding reviews cannot inherit stale rows.
        key = norm(path.stem)
        explicit_repo, explicit_clone = read_review_identity(path)
        if explicit_repo or explicit_clone:
            legacy_repo, legacy_clone = ident.get(key, ("", ""))
            row["public_repo"] = explicit_repo or legacy_repo
            row["clone_path"] = explicit_clone or derive_clone_path(explicit_repo) or legacy_clone
            joined += 1
            rows.append(row)
            for f in flags:
                all_flags.append((row["review_file"], f))
            continue
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
