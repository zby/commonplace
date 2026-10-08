"""One workflow engine, a shared set-run layer, and the analysis consumer above both."""

import ast
import subprocess
import sys
from pathlib import Path

import pytest

import commonplace

PACKAGE = Path(commonplace.__file__).resolve().parent


def test_data_modules_import_without_workflow_execution():
    subprocess.run([
        sys.executable, "-c",
        ("import sys; from commonplace.lib.agentic_analysis import sets, records, ledger; "
         "assert 'commonplace.workflow' not in sys.modules"),
    ], check=True)


@pytest.mark.parametrize("layer", ["workflow", "setrun"])
def test_lower_layers_do_not_import_the_analysis_consumer(layer):
    for path in (PACKAGE / layer).glob("*.py"):
        for node in ast.walk(ast.parse(path.read_text())):
            modules = ([node.module or ""] if isinstance(node, ast.ImportFrom) else
                       [item.name for item in node.names] if isinstance(node, ast.Import) else [])
            assert not any("agentic_analysis" in name for name in modules), path
