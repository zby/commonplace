"""One workflow engine, with the analysis consumer in its own package."""

import ast
import importlib
import subprocess
import sys
from pathlib import Path

import commonplace
from commonplace.lib.agentic_analysis.declaration import JOB_SET
from commonplace.workflow import load_job_set
from commonplace.workflow.declaration import CodeJob

PACKAGE = Path(commonplace.__file__).resolve().parent


def test_retired_execution_modules_are_absent():
    assert not (PACKAGE / "workflow_legacy").exists()
    for name in ("agentic_workflow", "agentic_finalize", "agentic_analysis",
                 "agentic_publication", "analysis_worktree",
                 "agentic_set", "agentic_records", "agentic_ledger"):
        assert not (PACKAGE / "lib" / f"{name}.py").exists()
    assert not list((PACKAGE / "lib").glob("agentic_job_*.py"))
    for name in ("finalize", "handoff", "publication"):
        assert not (PACKAGE / "cli" / f"agentic_analysis_{name}.py").exists()


def test_data_modules_import_without_workflow_execution():
    subprocess.run([
        sys.executable, "-c",
        ("import sys; from commonplace.lib.agentic_analysis import sets, records, ledger; "
         "assert 'commonplace.workflow' not in sys.modules"),
    ], check=True)


def test_generic_engine_does_not_import_the_analysis_consumer():
    for path in (PACKAGE / "workflow").glob("*.py"):
        for node in ast.walk(ast.parse(path.read_text())):
            modules = ([node.module or ""] if isinstance(node, ast.ImportFrom) else
                       [item.name for item in node.names] if isinstance(node, ast.Import) else [])
            assert not any("agentic_analysis" in name or "workflow_legacy" in name for name in modules), path


def test_all_declared_analysis_handlers_live_in_the_consumer_package():
    repo = PACKAGE.parents[1]
    jobs = load_job_set((repo / "kb" / JOB_SET).read_text())
    for job in jobs.jobs:
        if isinstance(job, CodeJob):
            assert job.handler.startswith("commonplace.lib.agentic_analysis.")
            module, _, function = job.handler.rpartition(".")
            assert callable(getattr(importlib.import_module(module), function))
