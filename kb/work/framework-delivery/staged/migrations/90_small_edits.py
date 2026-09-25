"""Changes of one or two lines, applied as exact search-and-replace pairs.

These are not staged as file copies (operator direction, 2026-09-25). Each pair
must match exactly once in its file; a mismatch stops the apply so the pair can
be rebased. CHANGES.md explains them.
"""

import subprocess
from pathlib import Path

ROOT = globals().get("ROOT") or Path.cwd()

EDITS: list[tuple[str, str, str, str]] = [
    # (file, old, new, why)
    (
        "tests/commonplace/lib/test_validation_unquoted_sources.py",
        '    type_path: str = "kb/types/note.md",',
        '    type_path: str = "note",',
        "global types are named by bare name",
    ),
    (
        "tests/commonplace/lib/test_validation_unquoted_sources.py",
        '        ("notes", "kb/types/note.md"),',
        '        ("notes", "note"),',
        "global types are named by bare name",
    ),
    (
        "src/commonplace/cli/review/resolve_criteria.py",
        "from commonplace.lib import frontmatter\n",
        "from commonplace.lib import frontmatter\nfrom commonplace.lib.library import artifact_file\n",
        "criteria may live in the installed library",
    ),
    (
        "src/commonplace/cli/review/resolve_criteria.py",
        "            criterion_file = repo_root / criterion_path\n",
        "            criterion_file = artifact_file(repo_root, criterion_path)\n",
        "criteria may live in the installed library",
    ),
    (
        "src/commonplace/review/acknowledgement.py",
        "from commonplace.freshness.transitions import InputObservation, ack_target_inputs\n",
        "from commonplace.freshness.transitions import InputObservation, ack_target_inputs\nfrom commonplace.lib.library import artifact_file\n",
        "criteria may live in the installed library",
    ),
    (
        "src/commonplace/review/acknowledgement.py",
        "        if not (repo_root / criterion_path).is_file():\n",
        "        if not artifact_file(repo_root, criterion_path).is_file():\n",
        "criteria may live in the installed library",
    ),
    (
        "src/commonplace/review/review_target_selector.py",
        "from commonplace.lib.hashing import content_sha256_for_text\n",
        "from commonplace.lib.hashing import content_sha256_for_text\nfrom commonplace.lib.library import artifact_file\n",
        "criteria may live in the installed library",
    ),
    (
        "src/commonplace/review/review_target_selector.py",
        "            if not (repo_root / criterion_path).is_file():\n",
        "            if not artifact_file(repo_root, criterion_path).is_file():\n",
        "criteria may live in the installed library",
    ),
    (
        "src/commonplace/review/review_target_selector.py",
        "            criterion_abs = repo_root / criterion_path\n",
        "            criterion_abs = artifact_file(repo_root, criterion_path)\n",
        "criteria may live in the installed library",
    ),
    (
        "tests/commonplace/review/test_collection_conformance.py",
        '    note_type: str = "kb/types/note.md",',
        '    note_type: str = "note",',
        "global types are named by bare name",
    ),
    (
        "tests/commonplace/cli/test_validate_notes.py",
        '                "stay outside the live knowledge graph\\ntype: kb/types/note.md\\n"',
        '                "stay outside the live knowledge graph\\ntype: note\\n"',
        "global types are named by bare name",
    ),
    (
        "tests/commonplace/cli/test_validate_notes.py",
        "description: Non-path frontmatter type should be rejected by the current path-valued contract\n",
        "description: A bare frontmatter type names a global type, so an unknown name must be rejected\n",
        "a bare name is now valid syntax for a global type",
    ),
    (
        "tests/commonplace/cli/test_validate_notes.py",
        '        "frontmatter.type: must start with kb/ or be file-relative (./ or ../): spec"',
        '        "frontmatter.type points to a missing type spec: spec"',
        "a bare name is now valid syntax for a global type",
    ),
    (
        "kb/types/note.md",
        "| `type` | Yes | `kb/types/note.md` |",
        "| `type` | Yes | `note` |",
        "global types are named by bare name",
    ),
    (
        "kb/types/text.md",
        "- `type: note` — the path that selects the base note contract.",
        "- `type: note` — the bare name that selects the base note contract.",
        "global types are named by bare name",
    ),
]

for rel, old, new, why in EDITS:
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise SystemExit(f"{rel}: expected exactly one match for {old!r} ({why})")
    path.write_text(text.replace(old, new), encoding="utf-8")
python_files = sorted({str(ROOT / rel) for rel, *_ in EDITS if rel.endswith(".py")})
if python_files:
    # Merge new imports into the blocks earlier migrations wrote.
    subprocess.run(["uv", "run", "--quiet", "ruff", "check", "--select", "I", "--fix", *python_files], cwd=ROOT, check=True)
print(f"small edits: applied {len(EDITS)}")
