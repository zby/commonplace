"""Retype this checkout's local snapshots to `type: snapshot` (ADR 087 draft).

One-off for clones of the Commonplace source checkout, which never run
`commonplace-init` (installed projects get the same migration from init). Run it
after pulling the commit that moved the source and report types into the global
types and re-pinned the ingests:

    uv run python scripts/migrate-snapshot-types.py

It rewrites only the capture's `type:` frontmatter line, so identical captures
reach identical bytes on every machine and match the pulled checksums. An ingest
that still pins a capture's old bytes (for example, a local uncommitted ingest)
is re-pinned; commit it. Running it again changes nothing. Delete this script
once no clone needs it.
"""

from __future__ import annotations

from pathlib import Path

from commonplace.lib.snapshot import migrate_snapshot_types

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    result = migrate_snapshot_types(ROOT / "kb")
    print(f"Retyped {len(result.rewritten_snapshots)} snapshot(s).")
    for path in result.repinned_ingests:
        print(f"Re-pinned (commit this): {path.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
