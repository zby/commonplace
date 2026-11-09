"""Default finalization through real prepared commands and isolated fake harnesses."""
from __future__ import annotations

import json
import signal
import threading
from pathlib import Path

import pytest

from commonplace.lib.agentic_analysis import automation as auto
from commonplace.lib.agentic_analysis.durable import save
from tests.commonplace.agentic_analysis.execution_fixtures import IDENTITY, git
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared_template as prepared_template,  # noqa: PLC0414 - immutable baseline fixture
)
from tests.commonplace.agentic_analysis.test_automation import (
    command_origin as command_origin,  # noqa: PLC0414 - local executable environment fixture
)
from tests.commonplace.agentic_analysis.test_automation import (
    controller_process,
    invoke,
    wait_for,
)
from tests.commonplace.agentic_analysis.test_automation import (
    scripted_queue as scripted_queue,  # noqa: PLC0414 - bounded command scheduler fixture
)


@pytest.mark.slow
def test_refused_publication_resumes_without_workers_and_failed_audit_does_not_veto(command_origin, capsys, tmp_path):
    origin, scenario, _ = command_origin
    scenario.write_text(json.dumps({"audit-failure": True}))
    dirty = origin / "operator-work.txt"
    dirty.write_text("operator work must not be staged or removed\n")
    before = git(origin, "rev-parse", "HEAD")
    state = tmp_path / "controller"
    code, record, err = invoke(capsys, "analyse", IDENTITY, "--state", str(state), "--model", "initiating-agent")
    assert code == 3, (record, err)
    item, = record["targets"]
    assert item["status"] == "published" and item["integration"]["state"] == "refused"
    assert item["result"]["inspection"]["advisory-audit"]["state"] == "failed"
    run = Path(item["run"])
    receipt = (run / "receipt.json").read_bytes()
    counts = {p.name: p.read_bytes() for p in scenario.with_name("counts").iterdir()}
    assert git(origin, "rev-parse", "HEAD") == before
    assert dirty.read_text() == "operator work must not be staged or removed\n"
    dirty.unlink()  # the operator's repair, in this test's private origin only
    code, resumed, err = invoke(capsys, "resume", str(state))
    assert code == 0, (resumed, err)
    integrated, = resumed["targets"]
    assert integrated["integration"]["state"] == "integrated"
    assert integrated["run"] == item["run"]
    assert (run / "receipt.json").read_bytes() == receipt
    assert {p.name: p.read_bytes() for p in scenario.with_name("counts").iterdir()} == counts
    tree = Path(item["worktree"])
    assert "Model: initiating-agent" in git(tree, "show", "-s", "--format=%B", "HEAD")
    assert git(origin, "status", "--porcelain") == ""


@pytest.mark.slow
def test_replacement_automatically_integrates_exact_incumbent_archive(command_origin, capsys, tmp_path):
    origin, _, _ = command_origin
    code, first, err = invoke(capsys, "analyse", IDENTITY, "--state", str(tmp_path / "first"))
    assert code == 0, (first, err)
    item = first["targets"][0]
    run = Path(item["run"])
    receipt = item["result"]["inspection"]["receipt"]
    relative = Path(receipt["destination"]).relative_to(item["worktree"])
    old = {p.name: p.read_bytes() for p in (origin / relative).iterdir()}
    receipt_bytes = (run / "receipt.json").read_bytes()
    code, second, err = invoke(capsys, "analyse", IDENTITY, "--state", str(tmp_path / "second"))
    assert code == 0, (second, err)
    next_item = second["targets"][0]
    assert next_item["integration"]["state"] == "integrated"
    assert next_item["run"] != item["run"]
    archive = origin / "kb/agentic-system-analyses/retained-archive" / run.name
    assert {p.name: p.read_bytes() for p in archive.iterdir()} == old
    next_receipt = next_item["result"]["inspection"]["receipt"]
    assert {p.name: p.read_bytes() for p in (origin / relative).iterdir()} == {
        p.name: p.read_bytes() for p in Path(next_receipt["destination"]).iterdir()}
    assert (run / "receipt.json").read_bytes() == receipt_bytes
    before = git(origin, "rev-parse", "HEAD")
    code, resumed, err = invoke(capsys, "resume", second["controller"])
    assert code == 0 and resumed["targets"][0]["integration"]["state"] == "integrated", err
    assert git(origin, "rev-parse", "HEAD") == before
    assert git(origin, "status", "--porcelain") == ""


def test_selected_method_without_protocol_refuses_before_controller_or_preparation(command_origin, tmp_path):
    origin, _, _ = command_origin
    module = origin / "src/commonplace/lib/agentic_analysis/execution.py"
    module.write_text(module.read_text().replace(f'INTEGRATION_PROTOCOL = "{auto.INTEGRATION_PROTOCOL}"', "# old protocol"))
    git(origin, "add", str(module))
    git(origin, "commit", "-m", "Fixture old committed method")
    state, trees = tmp_path / "state", tmp_path / "trees"
    with pytest.raises(ValueError, match="lacks the automatic integration protocol"):
        auto.create(origin, [{"source": IDENTITY}], profile="pi-sol", revision=None, state=state,
                    worktree_root=trees, concurrency=1, max_workers=3, timeout=60, require_clean_origin=False)
    assert not state.exists() and not trees.exists()


def test_legacy_controller_does_not_acquire_automatic_authority(scripted_queue):
    state, barriers, record = scripted_queue
    record["schema"] = auto.LEGACY_SCHEMA
    save(state / "controller.json", record)
    for item in record["targets"]:
        (barriers / f"{item['key']}.release").touch()
    result = auto.Controller(state).run()
    assert result["counts"] == {"published": 3, "local-complete": 1, "stopped": 2}
    assert all("integration" not in item for item in result["targets"])
    assert auto.Controller(state).run()["counts"] == result["counts"]


def automatic_queue(state, barriers, record):
    record["schema"] = auto.SCHEMA
    record["integration-policy"] = auto.INTEGRATION_PROTOCOL
    for item in record["targets"]:
        item["integration"] = {"state": "pending"}
        (barriers / f"{item['key']}.release").touch()
    save(state / "controller.json", record)


def test_finalization_is_serial_after_all_analysis_children_drain(scripted_queue):
    state, barriers, record = scripted_queue
    automatic_queue(state, barriers, record)
    hold = barriers / "integration-hold"
    hold.touch()
    controller = auto.Controller(state)
    thread = threading.Thread(target=controller.run)
    thread.start()
    keys = [item["key"] for item in record["targets"]]
    try:
        wait_for(lambda: (barriers / f"{keys[0]}.integration-started").exists())
        assert len(list(barriers.glob("*.finished"))) == 6
        assert len(list(barriers.glob("*.integration-started"))) == 1
        (barriers / f"{keys[0]}.integration-release").touch()
        wait_for(lambda: (barriers / f"{keys[3]}.integration-started").exists())
        assert not (barriers / f"{keys[4]}.integration-started").exists()
    finally:
        hold.unlink()
        thread.join(20)
    result = auto.report(state)
    assert auto.exit_code(result) == 2
    assert [item["integration"]["state"] for item in result["targets"]] == [
        "integrated", "not-applicable", "pending", "integrated", "integrated", "pending"]
    assert len(list(barriers.glob("*.integration-started"))) == 3
    assert auto.Controller(state).run()["counts"] == result["counts"]


@pytest.mark.parametrize("abrupt", [False, True])
def test_integration_child_drains_or_keeps_lease_after_controller_signal(scripted_queue, abrupt):
    state, barriers, record = scripted_queue
    automatic_queue(state, barriers, record)
    hold = barriers / "integration-hold"
    hold.touch()
    key = record["targets"][0]["key"]
    process = controller_process(state)
    try:
        wait_for(lambda: (barriers / f"{key}.integration-started").exists())
        if abrupt:
            process.kill()
            process.wait(timeout=10)
            resumed = auto.Controller(state).run()
            assert resumed["targets"][0]["status"] == "operator-attention"
            assert len(list(barriers.glob("*.integration-started"))) == 1
        else:
            process.send_signal(signal.SIGTERM)
            # A held child must not be abandoned or replaced by another effect.
            assert process.poll() is None
        (barriers / f"{key}.integration-release").touch()
        wait_for(lambda: (barriers / f"{key}.integration-finished").exists())
        if not abrupt:
            assert process.wait(timeout=20) == 3
            assert len(list(barriers.glob("*.integration-started"))) == 1
        hold.unlink()
        def settled():
            from commonplace.lib.agentic_analysis.durable import lease

            try:
                with lease(state / "leases" / key):
                    return True
            except ValueError:
                return False
        wait_for(settled)
        resumed = auto.Controller(state).run()
        assert auto.exit_code(resumed) == 2
        assert len(list(barriers.glob("*.integration-started"))) == 3
        assert resumed["targets"][0]["integration"]["state"] == "integrated"
    finally:
        hold.unlink(missing_ok=True)
        if process.poll() is None:
            process.kill()
        process.wait(timeout=10)
