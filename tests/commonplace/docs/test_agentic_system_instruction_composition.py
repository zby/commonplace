from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]


def test_collection_method_inputs_cover_discovered_contracts_and_exclude_outputs() -> None:
    from commonplace.lib.agentic_publication import METHOD_PATHS
    from commonplace.lib.agentic_workflow import JOBS, STATE_ROOT

    declared = [REPO_ROOT / value for value in METHOD_PATHS]

    def pinned(path: Path) -> bool:
        return any(path == item or (item.is_dir() and path.is_relative_to(item)) for item in declared)

    collection = REPO_ROOT / "kb/agentic-system-analyses"
    contracts = [collection / "COLLECTION.md"]
    # The old projection type is retained as history, outside the current method.
    contracts.extend(path for path in (collection / "types").iterdir()
                     if not path.name.startswith("generated-review."))
    assert not pinned(collection / "types/generated-review.md")
    assert not pinned(collection / "types/generated-review.schema.yaml")
    contracts.extend((collection / "instructions").glob("agentic-analysis-*.md"))
    contracts.extend((REPO_ROOT / JOBS).glob("*.md"))
    assert contracts and all(pinned(path) for path in contracts)
    assert all(path.exists() for path in declared)
    for area in ("state", "retained", "retained-archive", "reviews", "comparisons"):
        assert not pinned(collection / area / "example.md")
    assert REPO_ROOT / STATE_ROOT == collection / "state"
