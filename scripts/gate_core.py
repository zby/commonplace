from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

import frontmatter
from review_metadata import blob_sha_at_commit, read_blob, run_git
from review_state import extract_body_lines, has_frontmatter, is_index, list_reviewable_notes


ALLOWED_WATCHES = {"title", "description", "frontmatter", "body"}
REWRITE_PATTERN = re.compile(r"^rewrite\(([^)]+)\)$")
GATES_SECTION_PATTERN = re.compile(
    r"^## Gates\s*\n(.*?)(?=^## |\Z)",
    re.DOTALL | re.MULTILINE,
)


@dataclass(frozen=True)
class StalenessPolicy:
    mode: str
    threshold: float | None = None


@dataclass(frozen=True)
class GateDefinition:
    path: Path
    gate_id: str
    name: str
    lens: str
    watches: tuple[str, ...]
    staleness: StalenessPolicy


@dataclass(frozen=True)
class NoteRegions:
    path: Path
    rel_path: str
    text: str
    title: str
    description: str
    frontmatter_raw: str
    body_text: str


def parse_staleness(raw_value: object) -> StalenessPolicy:
    if not isinstance(raw_value, str) or not raw_value:
        raise ValueError("staleness must be a non-empty string")
    if raw_value == "changed":
        return StalenessPolicy(mode="changed")
    match = REWRITE_PATTERN.fullmatch(raw_value)
    if match is None:
        raise ValueError(f"unsupported staleness policy: {raw_value}")
    return StalenessPolicy(mode="rewrite", threshold=float(match.group(1)))


def _normalize_watches(raw_value: object) -> tuple[str, ...]:
    if not isinstance(raw_value, list) or not raw_value:
        raise ValueError("watches must be a non-empty list")

    watches: list[str] = []
    for item in raw_value:
        if not isinstance(item, str) or item not in ALLOWED_WATCHES:
            raise ValueError(f"unsupported watched region: {item!r}")
        watches.append(item)
    return tuple(watches)


def load_gate_definition(gates_root: Path, gate_id: str) -> GateDefinition:
    gate_path = gates_root / f"{gate_id}.md"
    if not gate_path.is_file():
        raise FileNotFoundError(f"Gate not found: {gate_id}")

    parsed = frontmatter.parse(gate_path.read_text(encoding="utf-8"))
    if not parsed.ok:
        raise ValueError(f"Invalid gate frontmatter in {gate_path}: {parsed.errors}")

    data = parsed.data
    loaded_gate_id = data.get("gate_id")
    if loaded_gate_id != gate_id:
        raise ValueError(
            f"gate_id mismatch in {gate_path}: expected {gate_id}, got {loaded_gate_id}"
        )
    lens = data.get("lens")
    if not isinstance(lens, str) or not lens:
        raise ValueError(f"Gate lens missing in {gate_path}")

    return GateDefinition(
        path=gate_path,
        gate_id=gate_id,
        name=str(data.get("name") or gate_path.stem.replace("-", " ").title()),
        lens=lens,
        watches=_normalize_watches(data.get("watches")),
        staleness=parse_staleness(data.get("staleness")),
    )


def load_all_gate_definitions(gates_root: Path) -> list[GateDefinition]:
    definitions: list[GateDefinition] = []
    for gate_path in sorted(gates_root.rglob("*.md")):
        rel = gate_path.relative_to(gates_root).with_suffix("").as_posix()
        definitions.append(load_gate_definition(gates_root, rel))
    return definitions


def parse_bundle_gate_ids(bundle_path: Path) -> list[str]:
    text = bundle_path.read_text(encoding="utf-8")
    match = GATES_SECTION_PATTERN.search(text)
    if match is None:
        raise ValueError(f"Missing ## Gates section in {bundle_path}")

    gate_ids: list[str] = []
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        gate_ids.append(stripped[2:].strip())
    if not gate_ids:
        raise ValueError(f"No gate ids listed in {bundle_path}")
    return gate_ids


def load_bundle_gate_ids(bundles_root: Path, bundle_id: str) -> list[str]:
    bundle_path = bundles_root / f"{bundle_id}.md"
    if not bundle_path.is_file():
        raise FileNotFoundError(f"Bundle not found: {bundle_id}")
    return parse_bundle_gate_ids(bundle_path)


def _extract_title(content: str) -> str:
    lines = frontmatter.strip(content).splitlines()
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("# "):
            return stripped[2:].strip()
        break
    return ""


def load_note_regions(
    note_path: Path,
    repo_root: Path,
    *,
    text: str | None = None,
) -> NoteRegions:
    note_text = text if text is not None else note_path.read_text(encoding="utf-8")
    parsed = frontmatter.parse(note_text)
    description = parsed.data.get("description", "")
    if description is None:
        description = ""

    return NoteRegions(
        path=note_path,
        rel_path=note_path.relative_to(repo_root).as_posix(),
        text=note_text,
        title=_extract_title(note_text),
        description=str(description),
        frontmatter_raw=frontmatter.extract_raw(note_text) or "",
        body_text="\n".join(extract_body_lines(note_text)),
    )


def compute_watched_hash(note: NoteRegions, watches: tuple[str, ...]) -> str:
    hasher = hashlib.sha1()
    for region in watches:
        hasher.update(region.encode("utf-8"))
        hasher.update(b"\0")
        if region == "title":
            value = note.title
        elif region == "description":
            value = note.description
        elif region == "frontmatter":
            value = note.frontmatter_raw
        elif region == "body":
            value = note.body_text
        else:
            raise ValueError(f"unsupported watched region: {region}")
        hasher.update(value.encode("utf-8"))
        hasher.update(b"\0")
    return hasher.hexdigest()


def non_body_watches(gate: GateDefinition) -> tuple[str, ...]:
    return tuple(region for region in gate.watches if region != "body")


def body_change_ratio(reviewed_text: str, current_text: str) -> float:
    reviewed_lines = extract_body_lines(reviewed_text)
    current_lines = extract_body_lines(current_text)
    baseline = max(len(reviewed_lines), len(current_lines), 1)

    import difflib

    matcher = difflib.SequenceMatcher(a=reviewed_lines, b=current_lines)
    matched_lines = sum(block.size for block in matcher.get_matching_blocks())
    return 1 - (matched_lines / baseline)


def read_note_text_at_commit(repo_root: Path, note_rel_path: Path, commit: str) -> str:
    blob_sha = blob_sha_at_commit(repo_root, commit, note_rel_path)
    if blob_sha is None:
        raise ValueError(
            f"Could not resolve {note_rel_path.as_posix()} at commit {commit}"
        )
    return read_blob(repo_root, blob_sha)


def path_changed_since_commit(repo_root: Path, note_rel_path: Path, commit: str) -> bool:
    result = run_git(
        repo_root,
        "diff",
        "--quiet",
        commit,
        "--",
        note_rel_path.as_posix(),
        check=False,
    )
    if result.returncode == 0:
        return False
    if result.returncode == 1:
        return True
    raise ValueError(
        f"Could not diff {note_rel_path.as_posix()} against commit {commit}"
    )


def resolve_reviewable_note_paths(
    repo_root: Path,
    raw_note_paths: list[str] | None,
) -> list[Path]:
    notes_root = repo_root / "kb" / "notes"
    if not raw_note_paths:
        return list_reviewable_notes(notes_root)

    resolved: list[Path] = []
    for raw_path in raw_note_paths:
        note_path = Path(raw_path)
        if not note_path.is_absolute():
            note_path = repo_root / note_path
        note_path = note_path.resolve()

        try:
            note_path.relative_to(notes_root.resolve())
        except ValueError as exc:
            raise ValueError(f"Note is outside kb/notes: {raw_path}") from exc

        if note_path.parent != notes_root.resolve():
            raise ValueError(f"Only top-level kb/notes/*.md files are reviewable: {raw_path}")
        if not note_path.is_file():
            raise ValueError(f"Note not found: {raw_path}")
        if is_index(note_path) or not has_frontmatter(note_path):
            raise ValueError(f"Note is not reviewable: {raw_path}")
        resolved.append(note_path)

    return sorted(resolved)
