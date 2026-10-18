"""The shared candidate checks on an artifact type other than the analysis."""
from __future__ import annotations

from types import SimpleNamespace

import pytest
import yaml

from commonplace.artifactrun import checks, handlers
from commonplace.artifactrun.run import _parse_type

pytestmark = pytest.mark.usefixtures("tmp_library")

ARTIFACT_TYPE = "pairs/types/pair.md"
PAIR = """---
type: types/type-spec.md
name: pair
description: A head and a body that repeats its run.
schema: ./pair.schema.yaml
layout:
  membership: closed
  roles:
    head:
      path: head.md
      type: pairs/types/head.md
    body:
      path: body.md
      type: pairs/types/body.md
      identity:
        - {from: head, fields: [run]}
      cites: [head]
      verifies: [head]
---
# Pair
"""


def member_type(name: str) -> bytes:
    return (f"---\ntype: types/type-spec.md\nname: {name}\ndescription: A {name}.\n"
            f"schema: ./{name}.schema.yaml\n---\n# {name}\n").encode()


def attempt(tmp_path, candidate: bytes, judged: list) -> SimpleNamespace:
    (tmp_path / "kb/pairs").mkdir(parents=True)
    (tmp_path / "kb/pairs/COLLECTION.md").write_text("# Pairs\n")
    schema = yaml.safe_dump({"type": "object"}).encode()
    files = {
        "pairs/COLLECTION.md": b"# Pairs\n",
        "reference/validation-contract.md": b"# Validation contract\n",
        "pairs/types/pair.schema.yaml": schema,
        "pairs/types/head.md": member_type("head"), "pairs/types/head.schema.yaml": schema,
        "pairs/types/body.md": member_type("body"), "pairs/types/body.schema.yaml": schema,
    }
    layout, relations = _parse_type(PAIR, ARTIFACT_TYPE)
    inputs = {"candidate": candidate,
              "head": b"---\ntype: pairs/types/head.md\nname: head\ndescription: Head.\nrun: R1\n---\n# Head\n"}
    return SimpleNamespace(
        run_dir=tmp_path / "kb/pairs/state/run", run_values={}, layout=layout, relations=tuple(relations),
        type_spec=ARTIFACT_TYPE, type_text=PAIR, read=inputs.get, read_files=lambda: dict(files),
        judge=lambda subject, **verdict: judged.append(verdict),
    )


def candidate(tmp_path, data: bytes, judged: list) -> tuple[SimpleNamespace, checks.Candidate]:
    """The body candidate with the head as its one partner, as the standard handler builds it."""
    pinned = attempt(tmp_path, data, judged)
    check = checks.Candidate(
        "body", data, {"head.md": pinned.read("head")}, tmp_path, None,
        run_dir=pinned.run_dir, layout=pinned.layout, relations=pinned.relations,
        type_spec=pinned.type_spec, criteria=handlers.criterion_bytes(pinned), run_values=pinned.run_values)
    return pinned, check


def body(run: str) -> bytes:
    # The body verifies the head, so it follows the verification protocol.
    return (f"---\ntype: pairs/types/body.md\nname: body\ndescription: Body.\nrun: {run}\n---\n# Body\n\n"
            "## Blockers\n\nnone\n\n## Limits\n\nnone\n").encode()


def test_a_matching_body_is_accepted_over_its_relations(tmp_path):
    judged = []
    pinned, check = candidate(tmp_path, body("R1"), judged)
    reasons = checks.review(check)
    handlers.judge(pinned, check, reasons, answered=None)
    assert reasons == []
    assert judged == [{"outcome": "accepted", "scope": ("body:cites:head", "body:identity:head"), "findings": ""}]


def test_a_body_that_breaks_identity_is_refused_with_findings(tmp_path):
    judged = []
    pinned, check = candidate(tmp_path, body("R2"), judged)
    handlers.judge(pinned, check, checks.review(check), answered=None)
    assert judged[0]["outcome"] == "refused"
    assert "identity field run" in judged[0]["findings"] and "## Blockers\n\nnone" in judged[0]["findings"]


def test_the_manifest_quotes_a_type_path_yaml_would_cut():
    spec = "types/custom #1.md"
    assert yaml.safe_load(checks.manifest(spec)) == {"type": spec}


def test_a_content_acceptance_never_covers_a_verifies_relation(tmp_path):
    judged = []
    pinned, check = candidate(tmp_path, body("R1"), judged)
    assert ("body", "head", "body:verifies:head") in check.relations
    handlers.judge(pinned, check, checks.review(check), answered=None)
    assert "body:verifies:head" not in judged[0]["scope"]
