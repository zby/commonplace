#!/usr/bin/env python3
"""Generate the frozen ASISAS-2026 experiment systems matrix.

This script is intentionally scoped to this directory. It reads reviews from
`asisas-2026-experiment/reviews/`, reads the Karpathy core membership artifact
from the same experiment directory, and writes `asisas-2026-experiment/systems.csv`.
It does not read the living `kb/agent-memory-systems/reviews/` tree or write the
living `kb/agent-memory-systems/systems.csv`.

Run from the repository root:

    python3 kb/agent-memory-systems/asisas-2026-experiment/scripts/build_systems_matrix.py
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

from systems_matrix_frozen import (
    COLUMNS, JOINED, PARSED, norm, parse_review_text,
)

SCRIPT = Path(__file__).resolve()
EXPERIMENT_DIR = SCRIPT.parents[1]
REPO_ROOT = SCRIPT.parents[4]
REVIEWS_DIR = EXPERIMENT_DIR / "reviews"
SYSTEMS_CSV = EXPERIMENT_DIR / "systems.csv"
KARPATHY_GIST_CORE_FILE = EXPERIMENT_DIR / "karpathy-gist-agent-memory-reproducible-core.md"
RELATED_SYSTEMS = REPO_ROOT / "related-systems"

# The frozen experiment contains code-grounded reviews only. The doc-grounded
# Mnemosyne member is recorded in the core-membership file but outside systems.csv.
REVIEWS_TIER = "code-grounded"


def parse_review(path: Path, source_tier: str) -> tuple[dict[str, str], list[str]]:
    review_file = str(path.relative_to(EXPERIMENT_DIR))
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


def github_repo_key(repo_url: str) -> str:
    """Normalised owner/repo key for GitHub repository URLs."""
    clean = re.sub(r"[#?].*$", "", repo_url.strip().removesuffix(".git").rstrip("/"))
    match = re.search(r"github\.com/([^/\s)]+)/([^/\s)]+)$", clean)
    if not match:
        return ""
    owner, repo = match.groups()
    return f"{owner.lower()}/{repo.lower()}"


def read_karpathy_gist_repo_keys() -> set[str]:
    """Return GitHub repos in the frozen Karpathy LLM-wiki gist core."""
    keys: set[str] = set()
    if not KARPATHY_GIST_CORE_FILE.exists():
        return keys
    text = KARPATHY_GIST_CORE_FILE.read_text(encoding="utf-8")
    for match in re.finditer(r"https://github\.com/[^\s)`>,]+", text):
        key = github_repo_key(match.group(0))
        if key:
            keys.add(key)
    return keys


def read_source_tier(path: Path) -> str | None:
    """Read the `source-tier` frontmatter value, or None if absent."""
    match = re.search(r"^source-tier:\s*(\S+)", path.read_text(encoding="utf-8"), re.MULTILINE)
    return match.group(1).strip() if match else None


def load_inventory() -> list[dict[str, str]]:
    """Load the prior frozen systems.csv for identity joins and preserved fields."""
    if not SYSTEMS_CSV.exists():
        return []
    legacy = {
        "system name": "system_name",
        "public repo": "public_repo",
        "path to cloned repo": "clone_path",
    }
    with SYSTEMS_CSV.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    return [{legacy.get(k, k): (v or "").strip() for k, v in row.items()} for row in rows]


def main() -> int:
    if not REVIEWS_DIR.is_dir():
        print(f"missing {REVIEWS_DIR}", file=sys.stderr)
        return 1

    inventory = load_inventory()
    karpathy_gist_repo_keys = read_karpathy_gist_repo_keys()

    def lastseg(value: str) -> str:
        return norm(re.sub(r"[#?].*$", "", value.rstrip("/")).split("/")[-1]) if value else ""

    ident: dict[str, tuple[str, str]] = {}
    for row in inventory:
        for key in {
            norm(row.get("system_name", "")),
            lastseg(row.get("public_repo", "")),
            lastseg(row.get("clone_path", "")),
        }:
            if key and key not in ident:
                ident[key] = (row.get("public_repo", ""), row.get("clone_path", ""))

    prior = {row["review_file"]: row for row in inventory if row.get("review_file")}

    review_files = []
    for path in sorted(REVIEWS_DIR.glob("*.md")):
        if ".replaced." in path.name or path.name in ("dir-index.md", "README.md"):
            continue
        review_files.append((path, read_source_tier(path)))

    rows: list[dict[str, str]] = []
    all_flags: list[tuple[str, str]] = []
    joined = 0
    for path, tier in review_files:
        row, flags = parse_review(path, REVIEWS_TIER)
        if tier is None:
            flags.append("source-tier: missing frontmatter")
        elif tier != REVIEWS_TIER:
            flags.append(
                f"source-tier: frontmatter says {tier!r}, expected {REVIEWS_TIER!r} for reviews/"
            )

        old = prior.get(row["review_file"])
        if old:
            for col in COLUMNS:
                if col not in PARSED and col not in JOINED and old.get(col):
                    row[col] = old[col]

        key = norm(path.stem)
        explicit_repo, explicit_clone = read_review_identity(path)
        if explicit_repo or explicit_clone:
            legacy_repo, legacy_clone = ident.get(key, ("", ""))
            row["public_repo"] = explicit_repo or legacy_repo
            row["clone_path"] = explicit_clone or derive_clone_path(explicit_repo) or legacy_clone
            joined += 1
        elif key in ident:
            row["public_repo"], row["clone_path"] = ident[key]
            joined += 1

        row["found_karpathy_llm_wiki_gist"] = (
            "1" if github_repo_key(row["public_repo"]) in karpathy_gist_repo_keys else "0"
        )
        rows.append(row)
        for flag in flags:
            all_flags.append((row["review_file"], flag))

    rows.sort(key=lambda row: (row["source_tier"], row["system_name"].lower()))
    with SYSTEMS_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    tiers: dict[str, int] = {}
    for row in rows:
        tiers[row["source_tier"]] = tiers.get(row["source_tier"], 0) + 1
    print(f"rows written: {len(rows)}  ({', '.join(f'{k}={v}' for k, v in sorted(tiers.items()))})")
    print(f"identity (repo/clone) joined: {joined}/{len(rows)}")
    print(f"flags: {len(all_flags)}")
    for review_file, flag in all_flags:
        print(f"  - {Path(review_file).name}: {flag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
