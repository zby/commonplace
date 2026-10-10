"""Load directory artifact bytes without running validation or traversal checks."""

from __future__ import annotations

import re
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Any

import yaml

from commonplace.lib.note_parser import ParsedDocument

MANIFEST_NAME = "ARTIFACT.yaml"


def type_manifest(type_spec: str) -> bytes:
    """A working artifact's manifest: its type alone, before any member is pinned."""
    return yaml.safe_dump({"type": type_spec}).encode()
SHA256 = re.compile(r"[0-9a-f]{64}\Z")


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate YAML keys before they can silently replace metadata."""

    def construct_mapping(self, node: yaml.Node, deep: bool = False) -> dict:
        pairs = self.construct_pairs(node, deep=deep)
        result = {}
        for key, value in pairs:
            try:
                if key in result:
                    raise ValueError(f"duplicate YAML key: {key!r}")
                result[key] = value
            except TypeError as exc:
                raise ValueError("YAML mapping keys must be scalar values") from exc
        return result


@dataclass(frozen=True)
class ArtifactMember:
    path: Path
    content: bytes
    document: ParsedDocument


@dataclass(frozen=True)
class DirectoryArtifact:
    path: Path
    content: bytes
    manifest: dict[str, Any]
    members: dict[str, ArtifactMember]

    def validation_object(self) -> dict[str, Any]:
        return {
            "manifest": self.manifest,
            "members": {
                name: member.document.to_validation_object()
                for name, member in self.members.items()
            },
        }


def member_paths(
    directory: Path, supplied_paths: Iterable[Path] = (), *, names: Iterable[str] | None = None,
) -> tuple[Path, ...]:
    """Visible children, or an explicit snapshot's exact direct Markdown names."""
    if names is not None:
        paths = set()
        for name in names:
            if (not isinstance(name, str) or Path(name).name != name or "\\" in name
                    or name.startswith(".") or not name.endswith(".md")):
                raise ValueError(f"snapshot member must name a direct Markdown file: {name!r}")
            paths.add(directory / name)
        return tuple(sorted(paths))
    paths = set(directory.iterdir()) if directory.is_dir() else set()
    paths.update(path for path in supplied_paths if path.parent == directory)
    return tuple(sorted(
        path for path in paths
        if path.parent == directory and path.suffix == ".md"
        and not path.name.startswith(".")
        and (not path.exists() or not path.is_dir() or path.is_symlink())
    ))


def load_directory_artifact(
    directory: Path,
    *,
    read: Callable[[Path], bytes],
    supplied_paths: Iterable[Path] = (),
    member_names: Iterable[str] | None = None,
    parse: Callable[[Path], ParsedDocument],
) -> DirectoryArtifact:
    """Read the manifest and all members from one caller-owned byte snapshot."""
    manifest_path = directory / MANIFEST_NAME
    if manifest_path.is_symlink():
        raise ValueError("artifact manifest must not be a symlink")
    content = read(manifest_path)
    try:
        manifest = yaml.load(content.decode("utf-8"), Loader=UniqueKeyLoader)
    except (yaml.YAMLError, UnicodeError) as exc:
        raise ValueError(f"invalid {MANIFEST_NAME}: {exc}") from exc
    if not isinstance(manifest, dict) or not isinstance(manifest.get("type"), str):
        raise TypeError("artifact manifest needs a mapping with a string type")
    metadata = manifest.get("members", {})
    if not isinstance(metadata, dict):
        raise TypeError("manifest members must be a mapping")
    members = {}
    for path in member_paths(directory, supplied_paths, names=member_names):
        if path.is_symlink() or path.resolve().parent != directory.resolve():
            raise ValueError(f"member {path.name}: symlinks are not supported")
        member_content = read(path)
        members[path.name] = ArtifactMember(path, member_content, parse(path))
    for name, entry in metadata.items():
        if (not isinstance(name, str) or Path(name).name != name or "\\" in name
                or name.startswith(".") or not name.endswith(".md")):
            raise ValueError(f"manifest member path must name a direct Markdown file: {name!r}")
        if not isinstance(entry, dict) or set(entry) - {"sha256"}:
            raise ValueError(f"manifest member {name}: only sha256 metadata is supported")
        if name not in members:
            raise ValueError(f"manifest member {name}: no discovered file")
        if "sha256" in entry:
            expected = entry["sha256"]
            if not isinstance(expected, str) or SHA256.fullmatch(expected) is None:
                raise ValueError(f"manifest member {name}: malformed SHA-256")
            if sha256(members[name].content).hexdigest() != expected:
                raise ValueError(f"manifest member {name}: SHA-256 mismatch")
    return DirectoryArtifact(directory, content, manifest, members)
