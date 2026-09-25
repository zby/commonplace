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
    (
        "kb/instructions/cp-skill-write-multistage/SKILL.md",
        "  and `kb/types/note.md`; an instruction goes to `kb/instructions/`. Reject",
        "  and `note`; an instruction goes to `kb/instructions/`. Reject",
        "global types are named by bare name",
    ),
    (
        "kb/instructions/cp-skill-write-multistage/SKILL.md",
        "`kb/instructions/assess-a-claim-bearing-artifact-against-external-literature.md`\n(or its installed Commonplace path).",
        "[assess-a-claim-bearing-artifact-against-external-literature](../assess-a-claim-bearing-artifact-against-external-literature.md),\nresolved from this skill's real location.",
        "skills run in place in the library and use relative links",
    ),
    (
        "kb/instructions/cp-skill-validate/SKILL.md",
        "run `kb/instructions/run-review-batches.md` with the `frontmatter` bundle.",
        "run [run-review-batches](../run-review-batches.md), resolved from this skill's real location, with the `frontmatter` bundle.",
        "skills run in place in the library and use relative links",
    ),
    (
        "kb/instructions/cp-skill-connect/SKILL.md",
        "`kb/reference/control-plane-goals.md` documents this always-loaded goal-frame invariant",
        "[Control-plane goals](../../reference/control-plane-goals.md) documents this always-loaded goal-frame invariant",
        "skills run in place in the library and use relative links",
    ),
    # Step 5, documentation: the library is read in place and global types have bare names.
    (
        "kb/reference/commands.md",
        "Create or extend a Commonplace project without overwriting existing files. See\n[architecture](./architecture.md) for the installed topology and package/user\nboundary.",
        "Create or extend a Commonplace project without overwriting its own files, and\nrewrite its machine-specific pointers into the installed library: skill stubs,\n`.commonplace/library.md`, and the Claude Code read rule. `--check` reports\nwhether those pointers are current without writing anything. See\n[architecture](./architecture.md) for the installed topology and package/user\nboundary.",
        "the library is read in place from the installed package, not copied into projects",
    ),
    (
        "kb/reference/validation-contract.md",
        "Imperative rules select types by canonical path, not by the type spec's bare `name`. An installed framework path under `kb/commonplace/` normalizes to its source identity, while a same-named collection-local type remains distinct ([ADR 048](./adr/048-imperative-type-rules-dispatch-by-canonical-path.md)).",
        "Imperative rules select types by type identity, not by the type spec's `name` field. A global type's identity is its bare name, and a collection-local type's is its normalized `kb/...` path, so a same-named collection-local type remains distinct. [ADR 048](./adr/048-imperative-type-rules-dispatch-by-canonical-path.md) introduced this keying when global types were still named by path.",
        "global types are named by bare name",
    ),
    (
        "kb/reference/agent-memory-coverage.md",
        "| Reusable memory distribution | `commonplace-init` installs reusable methodology under `kb/commonplace/` while leaving user collections project-owned. Shared types stay in `kb/types/`; promoted skills are linked into harness skill directories. | Local project authority and shipped-library upgrades still require operator judgment. |",
        "| Reusable memory distribution | The installed package carries reusable methodology, global types, review gates, and promoted skills as one library that every project reads in place; user collections stay project-owned. `commonplace-init` writes skill stubs and a routing file that point into the library. | A library upgrade applies in place with no project-level diff to review; local project authority still requires operator judgment. |",
        "the library is read in place from the installed package, not copied into projects",
    ),
    (
        "AGENTS.md",
        "The `cp-skill-*` family (`cp-skill-write`, `cp-skill-validate`, `cp-skill-connect`, etc.) is installed into `.claude/skills/` and `.agents/skills/` by `commonplace-init`; the harness loads them automatically.",
        "The `cp-skill-*` family (`cp-skill-write`, `cp-skill-validate`, `cp-skill-connect`, etc.) lives in `kb/instructions/`. In this checkout `.claude/skills/` and `.agents/skills/` hold committed relative symlinks to it, and the harness loads them automatically; installed projects instead receive stubs from `commonplace-init` that point to the same skills in the installed package.",
        "the library is read in place from the installed package, not copied into projects",
    ),
    (
        "AGENTS.md",
        "(`commonplace-*`, `llm-commonplace`, `src/commonplace/`, `kb/commonplace/`).",
        "(`commonplace-*`, `llm-commonplace`, `src/commonplace/`, `commonplace:` library identities).",
        "the library is read in place from the installed package, not copied into projects",
    ),
    (
        "kb/reference/README-REVIEW-SYSTEM.md",
        "in a source checkout, or under the installed framework gate catalog in generated projects.",
        "in a source checkout, or at `instructions/review-gates/{lens}/{name}.md` under the installed library root in a project, where their persisted identity is `commonplace:instructions/review-gates/{lens}/{name}.md`.",
        "the library is read in place from the installed package, not copied into projects",
    ),
    (
        "kb/reference/README-REVIEW-SYSTEM.md",
        "the persisted criterion identity is the type-spec path (for example `kb/types/definition.md`).",
        "the persisted criterion identity is the type spec's file identity: its repository path in this checkout (for example `kb/types/definition.md`), or `commonplace:types/definition.md` for a global type read from the installed library in a project.",
        "the library is read in place from the installed package, not copied into projects",
    ),
    (
        "kb/reference/README-REVIEW-SYSTEM.md",
        "Gates are typed `kb/types/review-gate.md`.",
        "Gates are typed `review-gate`.",
        "global types are named by bare name",
    ),
    (
        "src/commonplace/_data/templates/user-notes-COLLECTION.md",
        "A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract.",
        "A typed artifact in this collection may use a global Commonplace type, named by its bare name such as `type: note`, or a local type spec under this collection's `types/` directory, named by its path.",
        "global types are named by bare name",
    ),
    (
        "src/commonplace/_data/templates/user-reference-COLLECTION.md",
        "A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract.",
        "A typed artifact in this collection may use a global Commonplace type, named by its bare name such as `type: note`, or a local type spec under this collection's `types/` directory, named by its path.",
        "global types are named by bare name",
    ),
    (
        "src/commonplace/_data/templates/user-reports-COLLECTION.md",
        "A typed report may use a shared type under `kb/types/` or a local type under\n`kb/reports/types/`.",
        "A typed report may use a global Commonplace type, named by its bare name, or a\nlocal type under `kb/reports/types/`, named by its path.",
        "global types are named by bare name",
    ),
    (
        "src/commonplace/_data/templates/user-sources-COLLECTION.md",
        "A typed artifact in this collection may use a local type spec under\n`kb/sources/types/` or a shared type spec under `kb/types/`. Its `type:` value\nis the path to that contract.",
        "A typed artifact in this collection may use a local type spec under\n`kb/sources/types/`, named by its path, or a global Commonplace type, named by\nits bare name.",
        "global types are named by bare name",
    ),
    (
        "kb/notes/COLLECTION.md",
        "A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract.",
        "A typed artifact in this collection may use a global type spec under `kb/types/`, named by its bare name such as `type: note`, or a local type spec under this collection's `types/` directory, named by its path.",
        "global types are named by bare name",
    ),
    (
        "kb/reference/COLLECTION.md",
        "A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract.",
        "A typed artifact in this collection may use a global type spec under `kb/types/`, named by its bare name such as `type: note`, or a local type spec under this collection's `types/` directory, named by its path.",
        "global types are named by bare name",
    ),
    (
        "kb/instructions/COLLECTION.md",
        "A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract.",
        "A typed artifact in this collection may use a global type spec under `kb/types/`, named by its bare name such as `type: note`, or a local type spec under this collection's `types/` directory, named by its path.",
        "global types are named by bare name",
    ),
    (
        "kb/sources/COLLECTION.md",
        "A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract.",
        "A typed artifact in this collection may use a global type spec under `kb/types/`, named by its bare name such as `type: note`, or a local type spec under this collection's `types/` directory, named by its path.",
        "global types are named by bare name",
    ),
    (
        "kb/agentic-systems/COLLECTION.md",
        "A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract.",
        "A typed artifact in this collection may use a global type spec under `kb/types/`, named by its bare name such as `type: note`, or a local type spec under this collection's `types/` directory, named by its path.",
        "global types are named by bare name",
    ),
    (
        "kb/agent-memory-systems/COLLECTION.md",
        "A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract.",
        "A typed artifact in this collection may use a global type spec under `kb/types/`, named by its bare name such as `type: note`, or a local type spec under this collection's `types/` directory, named by its path.",
        "global types are named by bare name",
    ),
    (
        "kb/articles/COLLECTION.md",
        "A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract.",
        "A typed artifact in this collection may use a global type spec under `kb/types/`, named by its bare name such as `type: note`, or a local type spec under this collection's `types/` directory, named by its path.",
        "global types are named by bare name",
    ),
    (
        "kb/instructions/COLLECTION.md",
        "For a promoted skill, edit the canonical source under `kb/instructions/`, not its runtime projections. Inspect the promotion manifest and runtime projections only when the skill name, directory, promotion status, or packaged resources change.",
        "For a promoted skill, edit its directory under `kb/instructions/`; installed projects run it in place through the stubs `commonplace-init` writes, and this checkout through symlinks. Inspect the promotion manifest and the stub rendering only when the skill name, directory, promotion status, or frontmatter change.",
        "the library is read in place from the installed package, not copied into projects",
    ),
    (
        "src/commonplace/lib/project_paths.py",
        "    A collection is identified by a local COLLECTION.md file. This lets\n    installed library collections live under kb/commonplace/<collection>/ while\n    support directories such as kb/tasks/ are ignored unless they explicitly\n    opt in as collections.",
        "    A collection is identified by a local COLLECTION.md file, so support\n    directories such as kb/tasks/ are ignored unless they explicitly opt in as\n    collections.",
        "the library is read in place from the installed package, not copied into projects",
    ),
    (
        "src/commonplace/review/collection_conformance.py",
        "    `{path}` is the collection directory relative to `kb/`, so collections\n    under a non-collection namespace stay unambiguous: `collection/notes`\n    names `kb/notes/COLLECTION.md`, `collection/commonplace/notes` names\n    `kb/commonplace/notes/COLLECTION.md`.",
        "    `{path}` is the collection directory relative to `kb/`, so a collection\n    below a non-collection directory stays unambiguous: `collection/notes`\n    names `kb/notes/COLLECTION.md`.",
        "the library is read in place from the installed package, not copied into projects",
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
