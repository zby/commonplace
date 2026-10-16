"""Relocate retained GitHub analyses to owner-qualified names without changing bytes.

Run with uv run python scripts/migrate_analysis_publications.py [--apply]
[--record PATH]. Uses the relocation library for a single-pass backlink update.
Repeat after integrating a publication from a frozen pre-migration worktree.
Never changes run stores, source checkouts, archives or frozen worktrees.
"""
from __future__ import annotations

import argparse
import json
from hashlib import sha256
from pathlib import Path

import yaml

from commonplace.lib import relocation
from commonplace.lib.agentic_analysis.analyses import RETAINED_ROOT, publication_slug
from commonplace.lib.note_parser import parse_document


def file_hashes(directory: Path) -> dict[str, str]:
    files = list(directory.rglob("*"))
    if any(path.is_symlink() for path in files) or directory.is_symlink():
        raise ValueError(f"refusing symlink in {directory}")
    return {path.relative_to(directory).as_posix(): sha256(path.read_bytes()).hexdigest()
            for path in sorted(files) if path.is_file()}


def migration_plan(root: Path) -> list[dict]:
    """Check every manifest and all destinations before moving anything."""
    plan = []
    identities = set()
    destinations = set()
    for directory in sorted((root / RETAINED_ROOT).iterdir()):
        if directory.name.startswith("."):
            continue
        if not directory.is_dir() or directory.is_symlink():
            raise ValueError(f"not an ordinary retained directory: {directory}")
        hashes = file_hashes(directory)
        manifest = yaml.safe_load((directory / "ARTIFACT.yaml").read_text())
        expected = {name: value["sha256"] for name, value in manifest["members"].items()}
        if set(hashes) != {*expected, "ARTIFACT.yaml"} or any(hashes.get(k) != v for k, v in expected.items()):
            raise ValueError(f"manifest/file mismatch in {directory}")
        metadata = {}
        for role in ("memory", "overview"):
            document, error = parse_document((directory / f"{role}.md").read_text())
            if error or document is None or not document.frontmatter:
                raise ValueError(f"missing {role} identity in {directory}")
            metadata[role] = document.frontmatter
        identity = metadata["memory"]["source-identity"]
        destination = directory.with_name(publication_slug(identity, metadata["overview"]["system"]))
        if identity.lower() in identities or destination in destinations:
            raise ValueError(f"duplicate source or destination: {identity}")
        identities.add(identity.lower())
        destinations.add(destination)
        if destination != directory and destination.exists():
            raise ValueError(f"destination already exists: {destination}")
        plan.append({"source": identity, "run-id": metadata["overview"]["run-id"],
                     "old": directory.relative_to(root).as_posix(),
                     "new": destination.relative_to(root).as_posix(), "hashes": hashes})
    return plan


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--record", type=Path)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if args.apply and args.record and args.record.exists():
        raise ValueError(f"migration record already exists: {args.record}")
    plan = migration_plan(root)
    moves = [entry for entry in plan if entry["old"] != entry["new"]]
    print(f"{len(moves)} moves; {len(plan) - len(moves)} unchanged publications")
    for entry in moves:
        print(f"{entry['old']} -> {entry['new']}")
    if not args.apply:
        return 0
    # Compile all rewrites before the first mutation. A single pass avoids
    # scanning the KB once per publication, and rejects required member edits
    # rather than silently invalidating accepted hashes or repinning evidence.
    md_moves = {root / entry["old"] / name: root / entry["new"] / name
                for entry in moves for name in entry["hashes"] if name.endswith(".md")}
    updates = {}
    if moves:
        for path in relocation.find_repo_markdown_files(root):
            original = path.read_text(encoding="utf-8")
            if path in md_moves:
                updated, _ = relocation.rebase_and_rewrite_in_moved_file(original, path, md_moves[path], md_moves)
            else:
                updated, _ = relocation.rewrite_links_to_moved_files(original, path, md_moves)
            updated, _ = relocation.rewrite_source_notes(updated, repo_root=root, moves=md_moves)
            if updated != original:
                if path.is_relative_to(root / RETAINED_ROOT):
                    raise ValueError(f"relocation would change accepted bytes: {path}; stop for review")
                updates[path] = updated
    for entry in plan:
        if file_hashes(root / entry["old"]) != entry["hashes"]:
            raise ValueError(f"publication changed since preflight: {entry['old']}")
    for entry in moves:
        relocation.move_path(root / entry["old"], root / entry["new"])
    for path, updated in updates.items():
        path.write_text(updated, encoding="utf-8")
    for entry in plan:
        if file_hashes(root / entry["new"]) != entry["hashes"]:
            raise ValueError(f"publication bytes changed during migration: {entry['new']}")
    if args.record:
        args.record.parent.mkdir(parents=True, exist_ok=True)
        args.record.write_text(json.dumps({"moves": len(moves), "publications": plan,
                                          "all-bytes-unchanged": True}, indent=2) + "\n")
    print("All publication bytes and run IDs unchanged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
