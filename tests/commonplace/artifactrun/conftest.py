"""Register the generic artifact-run coordinator fixture."""

from collections.abc import Iterator
from pathlib import Path

import pytest

from commonplace.artifactrun import start_run
from tests.commonplace.artifactrun.handlers import INTERRUPT_ENV, LOG_ENV
from tests.commonplace.artifactrun.support import Coordinator, record_calls, toy_library


@pytest.fixture
def coordinator(tmp_path: Path, tmp_library: None, monkeypatch: pytest.MonkeyPatch) -> Iterator[Coordinator]:
    declaration, method = toy_library(tmp_path)

    log = tmp_path / "handlers.log"
    monkeypatch.setenv(LOG_ENV, str(log))
    monkeypatch.delenv(INTERRUPT_ENV, raising=False)
    record_calls(monkeypatch)

    run_dir = tmp_path / "runs" / "toy-1"
    start_run(run_dir, declaration, parameters={"subject": "toy"})
    coordinator = Coordinator(run_dir=run_dir, method=method, log=log)
    coordinator.advance()
    yield coordinator
