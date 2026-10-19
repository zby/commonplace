from pathlib import Path

import pytest

from commonplace.lib.agentic_analysis import analyses
from commonplace.lib.directory_layout import Finding, layout_findings
from commonplace.lib.note_parser import parse_document


def document(values: str):
    parsed, error = parse_document(f"---\n{values}\n---\n# Member\n")
    assert error is None and parsed is not None
    return parsed


def test_shipped_profiles_resolve_by_name() -> None:
    profiles = (Path(__file__).resolve().parents[3] / "kb" / analyses.WORKER_PROFILES).read_bytes()
    assert analyses.resolve_worker_profile(profiles, "pi-ultramarine") == {
        "profile": "pi-ultramarine",
        "harness": "pi",
        "launch-model": "paperinstruments/ultramarine-1-flash",
        "effort": "off",
    }
    with pytest.raises(ValueError, match=r"unknown worker profile 'nobody'; choose one of .*pi-ultramarine"):
        analyses.resolve_worker_profile(profiles, "nobody")


@pytest.mark.parametrize("identity,expected", [
    ("https://github.com/Pratiyush/llm-wiki", "pratiyush--llm-wiki"),
    ("https://github.com/kenhuangus/llm-wiki.git/", "kenhuangus--llm-wiki"),
    ("https://github.com/nvk/llm-wiki", "nvk--llm-wiki"),
    ("https://github.com/MehmetGoekce/llm-wiki", "mehmetgoekce--llm-wiki"),
    ("https://github.com/noirblue/IsaacCLupus_mnemosyn_spec", "noirblue--isaacclupus_mnemosyn_spec"),
    ("https://arxiv.org/html/2601.01885v1", "2601-01885v1"),
    ("https://example.invalid/llm-wiki", "llm-wiki"),
    ("local snapshot", "display-name"),
])
def test_publication_namespace_is_owner_qualified_only_for_github(identity, expected):
    assert analyses.publication_slug(identity, "Display Name") == expected


def test_publication_migration_does_not_change_run_slug():
    identity = "https://github.com/Pratiyush/llm-wiki"
    assert analyses.source_slug(identity, "Wiki") == "llm-wiki"
    assert analyses.publication_slug(identity, "Wiki") == "pratiyush--llm-wiki"


def test_identity_findings_belong_to_the_member_that_disagrees() -> None:
    layout = analyses.analysis_layout()
    types = {role.path: role.type for role in layout.roles.values()}
    members = {
        "boundary.md": document(f"type: {types['boundary.md']}\nrun-id: R\nreviewed-boundary: B\nresult-disposition: complete"),
        "runtime.md": document(f"type: {types['runtime.md']}\nrun-id: R\nreviewed-boundary: other"),
        "memory.md": document(f"type: {types['memory.md']}\nrun-id: R\nreviewed-boundary: B\nsource-identity: s"),
        "epistemic.md": document(f"type: {types['epistemic.md']}\nrun-id: other\nreviewed-boundary: B"),
        "memory-profile.md": document(
            f"type: {types['memory-profile.md']}\nrun-id: R\nreviewed-boundary: B\nsource-identity: t"),
    }
    findings = [finding for finding in layout_findings(layout, members) if not finding.absent]
    assert findings == [
        Finding("runtime", "runtime.md: identity field reviewed-boundary 'other' does not match boundary.md; expected 'B'"),
        Finding("epistemic", "epistemic.md: identity field run-id 'other' does not match boundary.md; expected 'R'"),
        Finding("memory-profile", "memory-profile.md: identity field source-identity 't' does not match memory.md; expected 's'"),
    ]






def test_boundary_disposition_selects_roles_before_overview_exists() -> None:
    layout = analyses.analysis_layout()
    assert layout.required.when_role == "boundary"
    assert layout.required.when_field == "result-disposition"
    for disposition in ("complete", "blocked", "out-of-scope"):
        members = {"boundary.md": document(f"result-disposition: {disposition}")}
        required, permitted = layout.requirement(members)
        expected = set(layout.roles) if disposition == "complete" else {"boundary", "overview"}
        assert required == permitted == expected
        # The overview repeats the boundary's disposition; it does not select roles.
        members["overview.md"] = document("result-disposition: complete")
        assert layout.requirement(members) == (expected, expected)
