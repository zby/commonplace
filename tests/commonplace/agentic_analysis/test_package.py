"""Import boundaries between the analysis data modules, the workflow and the headless runner."""

import ast
import subprocess
import sys
from pathlib import Path

import commonplace

HEADLESS = Path(commonplace.__file__).resolve().parent / "headless"


def imported_modules(path: Path) -> list[str]:
    """Absolute module names imported anywhere in one module; relative ones resolved in the package."""
    names = []
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.Import):
            names.extend(item.name for item in node.names)
        elif isinstance(node, ast.ImportFrom):
            base = node.module or ""
            if node.level:
                base = "commonplace.headless" + (f".{base}" if base else "")
            names.append(base)
    return names


def test_data_modules_import_without_the_workflow_or_headless_runner():
    subprocess.run([
        sys.executable, "-c",
        ("import sys; from commonplace.lib.agentic_analysis import analyses, records, ledger; "
         "assert 'commonplace.lib.agentic_analysis.workflow' not in sys.modules; "
         "assert not any(name.startswith('commonplace.headless') for name in sys.modules)"),
    ], check=True)


def test_headless_runner_uses_only_the_correction_checks_from_the_analysis_package():
    for path in HEADLESS.glob("*.py"):
        analysis = {name for name in imported_modules(path)
                    if name.startswith("commonplace.lib.agentic_analysis")}
        assert analysis <= {"commonplace.lib.agentic_analysis.checks"}, path
