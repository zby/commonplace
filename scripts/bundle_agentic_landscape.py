"""Freeze and verify landscape inputs read directly from main-analysis results."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory

from commonplace.lib.systems_matrix import csv_text, load_results

REPO_ROOT = Path(__file__).resolve().parents[1]
MATRIX = "matrix.csv"
SNAPSHOT = "snapshot.json"
MANIFEST = "MANIFEST.tsv"
METHOD_INPUTS = (
    "kb/agentic-systems/COLLECTION.md",
    "kb/reports/COLLECTION.md",
    "kb/types/agentic-system-analysis-result.md",
    "kb/types/agentic-system-analysis-result.schema.yaml",
    "kb/types/note.schema.yaml",
    "kb/types/note-base.schema.yaml",
    "kb/instructions/synthesize-agent-memory-landscape/SKILL.md",
    "kb/instructions/analyse-agentic-system/SKILL.md",
    "kb/instructions/COLLECTION.md",
    "AGENTS.md",
    "src/commonplace/lib/systems_matrix.py",
    "src/commonplace/lib/validation.py",
    "src/commonplace/lib/note_parser.py",
    "scripts/build_systems_matrix.py",
    "scripts/bundle_agentic_landscape.py",
    "pyproject.toml",
    "uv.lock",
)
RUNTIME_INPUTS = tuple(p for p in METHOD_INPUTS if p.endswith(".py"))


def digest(content: bytes) -> str:
    return sha256(content).hexdigest()


def relative(root: Path, path: Path) -> str:
    resolved = (root / path).resolve()
    value = resolved.relative_to(root).as_posix()
    if any(c in value for c in "\t\r\n"):
        raise ValueError("input path cannot contain tabs or newlines")
    return value


def manifest(files: dict[str, bytes]) -> bytes:
    return "".join(
        f"{digest(content)}\t{len(content)}\t{path}\n"
        for path, content in sorted(files.items())
    ).encode("utf-8")


def payload(root: Path) -> dict[str, bytes]:
    files = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"bundle contains a symlink: {path}")
        if path.is_file() and path != root / MANIFEST:
            files[path.relative_to(root).as_posix()] = path.read_bytes()
    return files


def require_runtime(root: Path) -> None:
    for path in RUNTIME_INPUTS:
        if (root / path).read_bytes() != (REPO_ROOT / path).read_bytes():
            raise ValueError(
                f"method differs: {path}; use the matching pinned checkout"
            )


def prepare(
    root: Path,
    output: Path,
    reviews: list[Path] | None = None,
    ontology: list[Path] | None = None,
) -> dict:
    root, output = root.resolve(), output.absolute()
    if output.exists() or output.is_symlink():
        raise ValueError("bundle destination already exists; choose a new directory")
    require_runtime(root)
    selected = None if reviews is None else [Path(relative(root, p)) for p in reviews]
    inputs = load_results(root, selected)
    extra = [relative(root, p) for p in ontology or []]
    if any(not p.startswith("kb/notes/") or not p.endswith(".md") for p in extra):
        raise ValueError("additional ontology inputs must be Markdown under kb/notes/")
    paths = set(METHOD_INPUTS) | set(inputs.hashes) | set(extra)
    files = {path: (root / path).read_bytes() for path in sorted(paths)}
    for path, expected in inputs.hashes.items():
        if digest(files[path]) != expected:
            raise ValueError(f"input changed while capturing: {path}")
    files[MATRIX] = csv_text(inputs).encode("utf-8")
    revision = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    snapshot = {
        "format": "commonplace.agentic-landscape.v1",
        "selection": "all-generated" if selected is None else "explicit",
        "reviews": [row["review_file"] for row in inputs.rows],
        "input_paths": sorted(paths),
        "ontology": sorted(set(extra)),
        "rows": len(inputs.rows),
        "source_tiers": dict(
            sorted(Counter(row["source_tier"] for row in inputs.rows).items())
        ),
        "analysis_cutoffs": sorted({row["analysis_cutoff"] for row in inputs.rows}),
        "matrix_sha256": digest(files[MATRIX]),
        "repository_revision": revision.stdout.strip()
        if revision.returncode == 0
        else None,
        "python_version": sys.version.split()[0],
    }
    files[SNAPSHOT] = (json.dumps(snapshot, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )
    files[".commonplace-validation-ignore"] = (
        b"Exact landscape input snapshot; validate through its owning bundle command.\n"
    )
    manifest_bytes = manifest(files)
    output.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix=".landscape-", dir=output.parent) as staging:
        staged = Path(staging)
        for path, content in {**files, MANIFEST: manifest_bytes}.items():
            target = staged / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        verify(staged, digest(manifest_bytes), source_root=root)
        if output.exists() or output.is_symlink():
            raise ValueError("bundle destination appeared during capture")
        staged.rename(output)
    return {**snapshot, "manifest_sha256": digest(manifest_bytes)}


def verify(
    bundle: Path, expected_sha256: str, *, source_root: Path | None = None
) -> dict:
    bundle = bundle.resolve()
    manifest_bytes = (bundle / MANIFEST).read_bytes()
    if digest(manifest_bytes) != expected_sha256:
        raise ValueError("manifest SHA-256 mismatch")
    files = payload(bundle)
    if manifest(files) != manifest_bytes:
        raise ValueError("bundle bytes differ from the pinned manifest")
    snapshot = json.loads(files[SNAPSHOT])
    if snapshot.get("format") != "commonplace.agentic-landscape.v1":
        raise ValueError("unsupported landscape bundle format")
    require_runtime(bundle)
    reviews = [Path(p) for p in snapshot["reviews"]]
    inputs = load_results(bundle, reviews)
    if csv_text(inputs).encode("utf-8") != files[MATRIX]:
        raise ValueError("matrix differs from bundled main results")
    if (
        snapshot["matrix_sha256"] != digest(files[MATRIX])
        or snapshot["rows"] != len(inputs.rows)
        or snapshot["source_tiers"]
        != dict(Counter(r["source_tier"] for r in inputs.rows))
        or snapshot["analysis_cutoffs"]
        != sorted({r["analysis_cutoff"] for r in inputs.rows})
    ):
        raise ValueError("snapshot population or matrix identity mismatch")
    if source_root is not None:
        source_root = source_root.resolve()
        for path in snapshot["input_paths"]:
            if relative(source_root, Path(path)) != path:
                raise ValueError(f"noncanonical source path: {path}")
            if (source_root / path).read_bytes() != files[path]:
                raise ValueError(f"source input changed: {path}")
        selected = None if snapshot["selection"] == "all-generated" else reviews
        current = load_results(source_root, selected)
        if csv_text(current).encode("utf-8") != files[MATRIX]:
            raise ValueError("selected population changed")
    return {**snapshot, "manifest_sha256": expected_sha256}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    capture = commands.add_parser("prepare")
    capture.add_argument("--output", type=Path, required=True)
    capture.add_argument("--source-root", type=Path, default=REPO_ROOT)
    capture.add_argument("--review", type=Path, action="append")
    capture.add_argument("--ontology", type=Path, action="append")
    check = commands.add_parser("verify")
    check.add_argument("bundle", type=Path)
    check.add_argument("--sha256", required=True)
    check.add_argument("--source-root", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "prepare":
            result = prepare(args.source_root, args.output, args.review, args.ontology)
        else:
            result = verify(args.bundle, args.sha256, source_root=args.source_root)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"landscape bundle rejected: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
