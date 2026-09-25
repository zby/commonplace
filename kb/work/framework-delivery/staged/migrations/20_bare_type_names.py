"""Name global types by bare name instead of path.

Rewrites, across the repository:
- `type:` lines that point at a global type (repo-relative `kb/types/X.md`, or a
  relative path resolving to it) to `type: X`, in Markdown frontmatter and examples,
  and inline code spans `` `type: kb/types/X.md` `` in prose;
- JSON-style frontmatter values `"type": "kb/types/X.md"` in Markdown;
- gate `requires_type:` values naming a global type, in scalar or list form;
- global type specs' `schema: kb/types/X.schema.yaml` to `schema: ./X.schema.yaml`;
- global schemas' `const: kb/types/X.md` pins to `const: X`;
- schema `$ref`s to a global schema from outside the library's types directory to
  `commonplace:types/X.schema.yaml`, resolved to the installed library;
- type-identity string literals `"kb/types/X.md"` in src/ to `"X"`.
- in tests/, fixture YAML lines `type: kb/types/X.md` inside strings and
  `"type": "kb/types/X.md"` values; real file paths such as those passed to
  copy helpers are left alone. Test files staged by hand are skipped.
"""

import re
from pathlib import Path

ROOT = globals().get("ROOT") or Path.cwd()
TYPES = ROOT / "kb" / "types"
GLOBAL = {p.stem for p in TYPES.glob("*.md") if p.stem not in {"README", "COLLECTION"}}
SKIP_PARTS = {".git", ".snapshots", ".venv", "node_modules"}
SKIP_PREFIXES = ("kb/reports/cache/", "kb/reports/state/")
TYPE_LINE = re.compile(r"^(\s*)type:\s*(\S+\.md)\s*$", re.M)
REF = re.compile(r'(\$ref"?\s*:\s*["\']?)([^"\'\s]+\.schema\.yaml)')


def _files(pattern: str):
    for path in ROOT.rglob(pattern):
        rel = path.relative_to(ROOT).as_posix()
        if SKIP_PARTS & set(path.parts) or rel.startswith(SKIP_PREFIXES) or not path.is_file():
            continue
        yield path


def _global_name(value: str, source: Path) -> str | None:
    target = ROOT / value if value.startswith("kb/") else (source.parent / value)
    target = target.resolve()
    if target.parent == TYPES.resolve() and target.stem in GLOBAL and target.suffix == ".md":
        return target.stem
    return None


def _rewrite(path: Path, text: str) -> None:
    if text != path.read_text(encoding="utf-8"):
        path.write_text(text, encoding="utf-8")
        counts["files"] += 1


counts = {"files": 0}

for path in _files("*.md"):
    text = path.read_text(encoding="utf-8")

    def bare(match: re.Match) -> str:
        name = _global_name(match.group(2), path)
        return f"{match.group(1)}type: {name}" if name else match.group(0)

    new = TYPE_LINE.sub(bare, text)
    # Gate requirements compare against the note's raw `type:` value, so they
    # name global types the same way: `requires_type: X` or a list of them.
    new = re.sub(
        r"^(\s*(?:requires_type:\s*|-\s+))kb/types/([a-z0-9-]+)\.md\s*$",
        lambda m: f"{m.group(1)}{m.group(2)}" if m.group(2) in GLOBAL else m.group(0),
        new,
        flags=re.M,
    ) if "requires_type:" in new else new
    # JSON-style frontmatter, as the agentic-analysis tooling writes it.
    new = re.sub(
        r'("type"\s*:\s*)"kb/types/([a-z0-9-]+)\.md"',
        lambda m: f'{m.group(1)}"{m.group(2)}"' if m.group(2) in GLOBAL else m.group(0),
        new,
    )
    # Inline code spans in prose, such as `type: kb/types/note.md`.
    new = re.sub(
        r"`type: kb/types/([a-z0-9-]+)\.md`",
        lambda m: f"`type: {m.group(1)}`" if m.group(1) in GLOBAL else m.group(0),
        new,
    )
    if path.parent.resolve() == TYPES.resolve():
        new = re.sub(r"^schema: kb/types/([a-z0-9-]+\.schema\.yaml)\s*$", r"schema: ./\1", new, flags=re.M)
    _rewrite(path, new)

for pattern in ("*.schema.yaml", "*.schema.json"):
    for path in _files(pattern):
        text = path.read_text(encoding="utf-8")
        in_library_types = path.parent.resolve() == TYPES.resolve()
        if in_library_types:
            text = re.sub(r"(const:\s*)kb/types/([a-z0-9-]+)\.md", r"\1\2", text)

        def ref(match: re.Match) -> str:
            target = (path.parent / match.group(2)).resolve()
            if in_library_types or target.parent != TYPES.resolve():
                return match.group(0)
            return f"{match.group(1)}commonplace:types/{target.name}"

        _rewrite(path, REF.sub(ref, text))

for path in _files("*.py"):
    rel = path.relative_to(ROOT).as_posix()
    if not rel.startswith("src/"):
        continue
    text = path.read_text(encoding="utf-8")
    new = re.sub(
        r'"kb/types/([a-z0-9-]+)\.md"',
        lambda m: f'"{m.group(1)}"' if m.group(1) in GLOBAL else m.group(0),
        text,
    )
    _rewrite(path, new)

# Tests staged by hand, which exercise the path form on purpose, and pure
# parser tests, whose type values are arbitrary strings.
HAND_STAGED_TESTS = {
    "tests/commonplace/lib/test_frontmatter.py",
    "tests/commonplace/lib/test_type_resolver.py",
    "tests/commonplace/docs/test_type_contract_integrity.py",
}
for path in _files("*.py"):
    rel = path.relative_to(ROOT).as_posix()
    if not rel.startswith("tests/") or rel in HAND_STAGED_TESTS:
        continue
    text = path.read_text(encoding="utf-8")
    new = re.sub(
        r"^(\s*)type: kb/types/([a-z0-9-]+)\.md\s*$",
        lambda m: f"{m.group(1)}type: {m.group(2)}" if m.group(2) in GLOBAL else m.group(0),
        text,
        flags=re.M,
    )
    new = re.sub(
        r'("type"\s*:\s*)"kb/types/([a-z0-9-]+)\.md"',
        lambda m: f'{m.group(1)}"{m.group(2)}"' if m.group(2) in GLOBAL else m.group(0),
        new,
    )
    _rewrite(path, new)

print(f"bare type names: rewrote {counts['files']} files")
