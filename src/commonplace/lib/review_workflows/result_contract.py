"""Complete worker-owned review fragments using the captured declared type.

There is one format, no footer/legacy-output adapter. Runtime field ownership
and exact quote checks supplement ordinary explicit artifact validation.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urldefrag

import yaml

from commonplace.lib import frontmatter
from commonplace.lib.library import library_root
from commonplace.lib.project_paths import collection_for_path, kb_root
from commonplace.lib.type_resolver import CriterionSnapshot
from commonplace.lib.validation import ValidationRun

TYPE = "types/review-result.md"
FORMAT = 2
WORKER_FIELDS = frozenset({"type", "findings", "outcome", "attack-outcome"})


class ControllerError(RuntimeError):
    """Broken controller inputs or evidence; never a worker correction request."""


class ReviewSnapshot(CriterionSnapshot):
    def read(self, path: Path) -> bytes:
        try:
            return super().read(path)
        except FileNotFoundError as error:
            raise ControllerError(str(error)) from error


def capture_contract(repo: Path | None = None) -> dict[str, bytes]:
    """Capture the library type/schema closure and project review collection contract.

    This walks only declared schema references, never operational evidence.
    External schemas and symlink escapes are refused.
    """
    root = library_root().resolve()
    captured: dict[str, bytes] = {}

    def take(path: Path) -> str:
        resolved = path.resolve()
        if not resolved.is_relative_to(root) or path.is_symlink():
            raise ValueError(f"review contract escapes library: {path}")
        name = resolved.relative_to(root).as_posix()
        captured[name] = resolved.read_bytes()
        return name

    spec = take(root / TYPE)
    parsed = frontmatter.parse(captured[spec].decode("utf-8"))
    if not parsed.ok or not isinstance(parsed.data.get("schema"), str):
        raise ValueError("review-result must declare its schema")

    def schema(path: Path) -> None:
        name = path.resolve().relative_to(root).as_posix()
        if name in captured:
            return
        take(path)
        data = yaml.load(captured[name], Loader=frontmatter.UniqueKeyLoader)

        def visit(value):
            if isinstance(value, dict):
                if "$id" in value or "$dynamicRef" in value:
                    raise ValueError("review schemas do not support alternate bases or dynamic references")
                ref = value.get("$ref")
                if isinstance(ref, str):
                    file, _ = urldefrag(ref)
                    if file:
                        if ":" in file or file.startswith("/"):
                            raise ValueError(f"review schema reference must be local: {ref}")
                        schema(path.parent / unquote(file))
                for child in value.values():
                    visit(child)
            elif isinstance(value, list):
                for child in value:
                    visit(child)
        visit(data)

    schema(root / Path(TYPE).parent / parsed.data["schema"])
    # Exercise the same closed resolver used for acceptance before any launch.
    snapshot = CriterionSnapshot(root, captured)
    snapshot.registry(root / Path(TYPE).parent / parsed.data["schema"])
    if repo is not None:
        try:
            collection = collection_for_path(repo / "kb/reports/state/review/review.md", repo)
        except ValueError:
            collection = None
        if collection is not None:
            path = collection / "COLLECTION.md"
            if path.is_symlink() or not path.resolve().is_relative_to(kb_root(repo).resolve()):
                raise ControllerError(f"review collection contract escapes repository: {path}")
            captured[path.relative_to(kb_root(repo)).as_posix()] = path.read_bytes()
        preflight(repo, captured)
    return captured


def preflight(root: Path, contracts: dict[str, bytes]) -> ReviewSnapshot:
    """Check schema closure and project validation dependencies before any model call."""
    snapshot = ReviewSnapshot(kb_root(root), contracts)
    try:
        spec = snapshot.frontmatter(snapshot.root / TYPE)
        if not spec.ok or not isinstance(spec.data.get("schema"), str):
            raise ControllerError("invalid captured review-result type")
        snapshot.registry(snapshot.root / Path(TYPE).parent / spec.data["schema"])
        anchor = root / "kb/reports/state/review/review.md"
        try:
            governing = collection_for_path(anchor, root) / "COLLECTION.md"
        except ValueError:
            governing = None
        if governing is not None and not snapshot.frontmatter(governing).ok:
            raise ControllerError(f"invalid captured collection frontmatter: {governing}")
        probe = ValidationRun(repo_root=root, paths=(), criteria=snapshot)
        probe.unquoted_source_limit(anchor)
    except (OSError, ValueError, TypeError) as error:
        raise ControllerError(f"invalid captured validation context: {error}") from error
    return snapshot


def fingerprint(contents: dict[str, bytes]) -> str:
    manifest = {name: hashlib.sha256(data).hexdigest() for name, data in sorted(contents.items())}
    return hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()


def render(data: dict, body: str) -> str:
    return "---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True) + "---\n" + body


@dataclass(frozen=True)
class Candidate:
    text: str
    data: dict
    body: str
    warnings: tuple[str, ...]


def validate_saved(root: Path, path: Path, text: str, *, contracts: dict[str, bytes] | None = None):
    parsed = frontmatter.parse(text)
    if not parsed.ok:
        raise ValueError("; ".join(parsed.errors))
    if parsed.data.get("type") != TYPE or parsed.data.get("format") != FORMAT:
        raise ValueError("unsupported review-result format; archive old results and start a new review")
    snapshot = preflight(root, contracts if contracts is not None else capture_contract(root))
    captured = {path.resolve(): text}
    for key in ("target-capture", "raw-output"):
        name = parsed.data.get(key)
        if not isinstance(name, str):
            continue
        rel = Path(name)
        evidence = root / rel
        if rel.is_absolute() or ".." in rel.parts or not evidence.resolve().is_relative_to(root.resolve()):
            raise ControllerError(f"{key}: controller evidence path escapes repository")
        try:
            content = evidence.read_bytes()
        except OSError as error:
            raise ControllerError(f"{key}: missing retained evidence: {error}") from error
        hash_key = "target-sha256" if key == "target-capture" else "raw-output-sha256"
        if hashlib.sha256(content).hexdigest() != parsed.data.get(hash_key):
            raise ControllerError(f"{key}: retained evidence hash mismatch")
        captured[evidence.resolve()] = content
    report = ValidationRun(repo_root=root, paths=(path,), content_overrides=captured,
                           criteria=snapshot).validate(path)
    if report.fails:
        raise ValueError("; ".join(report.fails))
    return report


def complete(root: Path, path: Path, fragment: str, *, metadata: dict,
             target: str, contracts: dict[str, bytes]) -> Candidate:
    parsed = frontmatter.parse(fragment)
    if not parsed.ok:
        raise ValueError("; ".join(parsed.errors))
    if parsed.data.get("type") != TYPE:
        raise ValueError(f"worker output must declare type: {TYPE}")
    reserved = parsed.data.keys() - WORKER_FIELDS
    if reserved:
        raise ValueError(f"worker supplied controller-owned or unknown fields: {', '.join(sorted(reserved))}")
    body = frontmatter.strip(fragment)
    if metadata.keys() & WORKER_FIELDS:
        raise ControllerError("controller metadata overlaps worker-owned content")
    if fingerprint(contracts) != metadata["contract-sha256"]:
        raise ControllerError("supplied contract does not match its captured digest")
    if hashlib.sha256(target.encode("utf-8")).hexdigest() != metadata["target-sha256"]:
        raise ControllerError("supplied target does not match the captured-target digest")
    data = {**parsed.data, **metadata, "format": FORMAT}
    text = render(data, body)
    report = validate_saved(root, path, text, contracts=contracts)
    return Candidate(text, data, body, tuple(report.warns))
