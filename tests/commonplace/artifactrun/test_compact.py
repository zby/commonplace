"""The compact loader's derivations that the toy scenarios do not reach."""

from __future__ import annotations

from pathlib import Path

import yaml

from commonplace.artifactrun.compact import expand, type_closure
from tests.commonplace.artifactrun.support import compact_plan, toy_library


def expansion(tmp_path: Path, data: dict) -> dict:
    _, method = toy_library(tmp_path, compact=True)
    jobs = {job["name"] for job in expand(data, library=tmp_path / "kb", plan_dir=method)["jobs"]}
    assert "apply-verification" in jobs
    return {job["name"]: job for job in expand(data, library=tmp_path / "kb", plan_dir=method)["jobs"]}


def test_a_derived_apply_gets_the_frozen_source_role_live_when_the_verifier_did_not_read_it(tmp_path):
    data = {**compact_plan(), "frozen-source": "brief"}  # The toy verifier reads its subjects only.
    apply = expansion(tmp_path, data)["apply-verification"]
    assert apply["options"]["frozen-source"] == "brief"
    assert apply["inputs"]["brief"] == {"address": "role", "source": "brief"}
    assert "brief-seen" not in apply["inputs"]


def test_a_derived_apply_uses_the_handed_frozen_source_when_the_verifier_read_it(tmp_path):
    data = {**compact_plan(), "frozen-source": "brief"}
    verifier = next(entry for entry in data["jobs"] if entry.get("role") == "verification")
    verifier["reads"] = {**verifier["reads"], "brief": "required"}
    apply = expansion(tmp_path, data)["apply-verification"]
    assert apply["inputs"]["brief-seen"] == {"address": "handed", "source": "verifier-attempt:brief"}
    assert "brief" not in apply["inputs"], "one input holds the role"


def test_the_type_closure_follows_library_root_schema_references(tmp_path):
    toy_library(tmp_path)
    types = tmp_path / "kb" / "types"
    (types / "base.schema.yaml").write_text(yaml.safe_dump({"type": "object"}), encoding="utf-8")
    schema = yaml.safe_load((types / "toy-report.schema.yaml").read_text(encoding="utf-8"))
    schema["allOf"] = [{"$ref": "commonplace:types/base.schema.yaml#/definitions/x"}]
    (types / "toy-report.schema.yaml").write_text(yaml.safe_dump(schema), encoding="utf-8")
    closure = type_closure(tmp_path / "kb", ["types/toy-report.md"])
    assert closure == ["types/toy-report.md", "types/toy-report.schema.yaml", "types/base.schema.yaml"]
