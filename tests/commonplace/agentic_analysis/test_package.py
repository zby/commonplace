"""One artifact-run package with a pure core, and the analysis consumer above it."""

import ast
import subprocess
import sys
from pathlib import Path

import commonplace

PACKAGE = Path(commonplace.__file__).resolve().parent
ARTIFACTRUN = PACKAGE / "artifactrun"
CORE = ("plan", "run", "store", "handouts", "engine")
REUSE = ("checks", "sources", "effects", "worktree", "report")
# The Commonplace modules the core imports today; widening this set is a design change.
CORE_LIBRARY_IMPORTS = {
    "commonplace.lib.directory_artifact",
    "commonplace.lib.directory_layout",
    "commonplace.lib.library",
    "commonplace.lib.note_parser",
    "commonplace.lib.reading_batches",
}


def imported_modules(path: Path) -> list[str]:
    """Absolute module names imported anywhere in one module; relative ones resolved in the package."""
    names = []
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.Import):
            names.extend(item.name for item in node.names)
        elif isinstance(node, ast.ImportFrom):
            base = node.module or ""
            if node.level:
                base = "commonplace.artifactrun" + (f".{base}" if base else "")
            # `from package import module` imports the module too.
            names.append(base)
            names.extend(f"{base}.{item.name}" for item in node.names)
    return names


def test_data_modules_import_without_artifact_run_execution():
    subprocess.run([
        sys.executable, "-c",
        ("import sys; from commonplace.lib.agentic_analysis import sets, records, ledger; "
         "assert 'commonplace.artifactrun' not in sys.modules"),
    ], check=True)


def test_artifactrun_does_not_import_the_analysis_consumer():
    for path in ARTIFACTRUN.glob("*.py"):
        assert not any("agentic_analysis" in name for name in imported_modules(path)), path


def test_core_imports_no_validation_reuse_modules_or_git():
    reuse = {f"commonplace.artifactrun.{name}" for name in REUSE}
    library = set()
    for name in CORE:
        path = ARTIFACTRUN / f"{name}.py"
        for module in imported_modules(path):
            assert module not in reuse, (path, module)
            assert not module.startswith("commonplace.lib.validation"), (path, module)
            assert module.split(".")[0] not in {"subprocess", "git"}, (path, module)
            if module.startswith("commonplace.") and not module.startswith("commonplace.artifactrun"):
                library.add(module)
    # `from commonplace.lib.x import name` also records `commonplace.lib.x.name`; keep the modules.
    library = {name for name in library if name.rsplit(".", 1)[0] not in library}
    assert library == CORE_LIBRARY_IMPORTS
