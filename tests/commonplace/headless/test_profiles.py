"""The model name is shared, but the grant is selected by the workflow."""

from pathlib import Path

import pytest
import yaml

from commonplace.headless.profiles import WORKER_PROFILES, resolve_profile

ROSTER = Path(__file__).resolve().parents[3] / "kb" / WORKER_PROFILES


def test_one_identity_addition_is_visible_to_every_granted_workflow():
    config = yaml.safe_load(ROSTER.read_bytes())
    config["profiles"]["example"] = {"harness": "claude-code", "launch-model": "example-model", "effort": "medium"}
    data = yaml.safe_dump(config).encode()
    profiles = {workflow: resolve_profile(data, "example", workflow)[1] for workflow in config["workflows"]}
    assert {(p.harness, p.launch_model, p.effort) for p in profiles.values()} == {
        ("claude-code", "example-model", "medium")}
    assert "Bash(git commit:*)" in profiles["task"].flags["allowed-tools"]
    for mode in ("review", "sub-worker"):
        assert "Bash" in profiles[mode].flags["disallowed-tools"]
        assert "git commit" not in profiles[mode].flags["allowed-tools"]
        assert f"current/{mode}/" in profiles[mode].flags["allowed-tools"]


def test_missing_grant_refuses_and_identity_cannot_supply_flags():
    data = ROSTER.read_bytes()
    with pytest.raises(ValueError, match="no task grant"):
        resolve_profile(data, "pi-sol", "task")
    config = yaml.safe_load(data)
    config["profiles"]["opus"]["flags"] = {"permission-mode": "acceptEdits"}
    with pytest.raises(ValueError, match="needs only"):
        resolve_profile(yaml.safe_dump(config).encode(), "opus", "sub-worker")
