"""Discriminating examples for classification-revision plan cases 1–13.

Everything here is synthetic, not evidence about any external system. Expected
semantic findings are authored fixture judgments. Real checks below establish
shape, canonical references, projection and public-text contracts, NOT that a
record proves its classification. Declared-input tests keep that judgment
assigned to the independent verifier; no toy source classifier stands in for it.
"""

import csv
import json
from copy import deepcopy
from dataclasses import dataclass
from io import StringIO

import pytest

from commonplace.lib import systems_matrix as sm
from commonplace.lib.agentic_analysis.records import (
    amendment_index,
    anchor,
    conclusion_status_errors,
    route_field_errors,
    section,
)
from commonplace.lib.validation import validate_draft_in_role
from scripts import analyze_matrix as stats
from tests.commonplace.agentic_analysis.fixtures import (
    artifact_record_errors,
    comparison_schema,
    frontmatter,
    member_fixture,
    repin,
    replace_frontmatter,
)


@dataclass(frozen=True)
class Part:
    handle: str
    scope: str
    facts: str
    values: tuple[str, ...] = ()
    assessment: str = "known"
    basis: str = "wired"
    limit: str = "The synthetic inventory covers only this named mechanism."
    kind: str = "RTE"

    @property
    def identifier(self):
        return f"MEM-{self.kind}-{self.handle}"


def unknown(handle, scope, missing, *, assessment="not-determinable", kind="OBJ"):
    return Part(handle, scope, missing, assessment=assessment, limit=missing, kind=kind)


def axis(*parts, assessment="known"):
    return assessment, parts


# These are explicit expected semantic findings, not outputs of a classifier.
# Every opaque alternative specifies a missing fact and the conclusion prevented.
CASES = [
    pytest.param({
        "write_agency": axis(
            Part("curator-admit", "Curator admission", "Software admits generated content without per-content human approval.", ("automatic",)),
            unknown("initial-sheet", "Initial sheet admission", "Caller identity and approval policy are inaccessible; human control and complete agency coverage cannot be determined."),
            assessment="partial"),
    }, {"write_agency": ["automatic"]}, id="01-curator-and-unknown-initial-sheet"),
    pytest.param({
        "write_agency": axis(
            Part("operator-install", "Initial installation", "A human explicitly approves the supplied content; software performs the disk write.", ("manual",)),
            Part("later-update", "Subsequent update", "A human starts the workflow, but the model subsequently admits each update without human approval.", ("automatic",))),
    }, {"write_agency": ["automatic", "manual"]}, id="02-operator-install-and-automatic-updates"),
    pytest.param({
        "write_agency": axis(
            Part("api-install", "Automated API installation", "The caller is a scheduled software service and admits content without any human decision.", ("automatic",)),
            unknown("caller-install", "Separate generic-caller API", "The API says caller, but caller identity and per-content control were not established; manual admission cannot be concluded."),
            assessment="partial"),
    }, {"write_agency": ["automatic"]}, id="03-api-caller-is-not-human"),
    pytest.param({
        "write_agency": axis(
            Part("checkpoint-read", "Operator checkpoint read", "The operator selects an existing checkpoint; this path only reads and never replaces content.", assessment="inapplicable", limit="Read-only operation; no write admission to classify."),
            Part("checkpoint-replace", "Separate checkpoint replacement", "The operator explicitly approves replacement content in a separate write operation.", ("manual",))),
        "read_back_direction": axis(Part("requested-read", "Requested checkpoint return", "The operator requests an existing checkpoint for a later consumer; delivery fulfills that request.", ("pull",))),
        "read_back_signal": axis(assessment="inapplicable"),
    }, {"write_agency": ["manual"], "read_back_direction": ["pull"], "read_back_signal": []}, id="04-checkpoint-read-versus-replacement"),
    pytest.param({
        "lineage": axis(
            Part("trace-derive", "Derived session summary", "Stored conversational turns are compressed into a retained summary; this derivation is wired.", ("trace-extracted",)),
            unknown("initial-origin", "Initial sheet provenance", "Initial content has no producer links; authored versus imported provenance cannot be established."),
            unknown("embedding-origin", "Embedding provenance", "Provider embedding production is opaque; the derivation path cannot be classified."),
            assessment="partial"),
    }, {"lineage": ["trace-extracted"]}, id="05-known-derivation-opaque-provenance"),
    pytest.param({
        "representational_form": axis(
            Part("text-payload", "Checkpoint prose consumed by model", "Natural-language guidance is interpreted by a later model invocation.", ("natural-language",), kind="OBJ"),
            Part("cursor-fields", "Checkpoint cursor consumed by fixed code", "Localized cursor fields have fixed symbolic selection rules.", ("symbolic",), kind="OBJ"),
            unknown("opaque-payload", "Provider payload", "Only a display summary is readable; consumed payload encoding is inaccessible, preventing classification."),
            assessment="partial"),
        "storage_substrate": axis(
            Part("checkpoint-file", "Local checkpoint parts", "Both prose and cursor fields persist in files, independently of their different encodings.", ("files",), kind="OBJ"),
            unknown("provider-store", "Opaque provider state", "The backing store is inaccessible; storage substrate and complete inventory remain unresolved."),
            assessment="partial"),
    }, {"representational_form": ["natural-language", "symbolic"], "storage_substrate": ["files"]}, id="06-mixed-parts-and-opaque-provider"),
    pytest.param({
        "behavioral_authority": axis(
            Part("answer-consumer", "Retained session object at answering agent", "One retained session object supplies reference content to an answering agent.", ("knowledge",)),
            Part("update-consumer", "Same session object at guidance updater", "The same object feeds an automatic durable-guidance update, a different consumer and effect.", ("learning",)),
            Part("rank-consumer", "Same session object at retrieval scorer", "Fixed code scores the same object's text to rank retrieval candidates.", ("ranking",))),
        "trace_learning": axis(Part("guidance-update", "Automatic guidance write and later agent", "Session traces feed automatic durable guidance production; a later agent reads that guidance. No capacity comparison was performed.", ("yes",))),
        "trace_source": axis(Part("session-input", "Original input to guidance update", "The input is recorded conversational turns, not merely an adapter label.", ("session-logs",))),
    }, {"behavioral_authority": ["knowledge", "learning", "ranking"], "trace_learning": ["yes"], "trace_source": ["session-logs"]}, id="07-one-object-distinct-consumers"),
    pytest.param({
        "curation_operations": axis(
            Part("compress-turns", "Inspected compression", "Existing claims are selected and compressed; no new claim is established by the inspected transformation.", ("consolidate",)),
            unknown("synthesis-request", "Prompt named synthesize", "The prompt requests a new claim, but output meaning is unavailable; implemented synthesis cannot be established.", kind="RTE"),
            assessment="partial"),
    }, {"curation_operations": ["consolidate"]}, id="08-requested-synthesis-not-implemented-proof"),
    pytest.param({
        "read_back_direction": axis(
            Part("request-return", "Request and automatic fulfillment", "A caller requests retained material; software selects and delivers it in fulfillment of that request.", ("pull",)),
            Part("unsolicited-supply", "Independent hook supply", "A hook supplies material to the next invocation without a consumer request.", ("push",)),
            unknown("alternate-delivery", "Alternative delivery", "Trigger and request relationship are inaccessible; its direction cannot be determined.", kind="RTE"),
            assessment="partial"),
        "read_back_signal": axis(
            Part("hook-selector", "Hook selection", "The hook matches the active task ID against retained parts and selects only matching parts for unsolicited delivery.", ("identifier",)),
            unknown("alternate-selector", "Alternative selector", "Selector inputs are inaccessible; a known pull route does not make this branch inapplicable.", kind="RTE"),
            assessment="partial"),
    }, {"read_back_direction": ["pull", "push"], "read_back_signal": ["identifier"]}, id="09-request-selection-delivery-and-alternative"),
    pytest.param({
        "trace_learning": axis(
            Part("summary-update", "Trace-fed continuation summary", "Automatic production consumes traces, retains guidance, and supplies a later invocation; this does not establish improved capacity.", ("yes",)),
            Part("static-branch", "Inspected static branch", "Search of static/ at fixture revision found no trace-fed update or later derived consumer.", ("no",), kind="ABS"),
            unknown("alternate-update", "Opaque update branch", "Durability and later consumption are inaccessible; qualifying trace learning is unresolved.", kind="RTE"),
            assessment="partial"),
        "trace_source": axis(
            Part("mixed-input", "Summary update original input", "The update consumes recorded conversational turns and tool results; an event adapter only wraps these inputs.", ("session-logs", "tool-traces")),
            unknown("opaque-input", "Included opaque update input", "Original provenance is inaccessible; no event-stream or trajectory category can be inferred from the adapter name."),
            assessment="partial"),
    }, {"trace_learning": ["yes"], "trace_source": ["session-logs", "tool-traces"]}, id="10-qualifying-update-mixed-and-opaque-inputs"),
    pytest.param({
        "curation_operations": axis(
            Part("curation-search", "Inspected curation boundary", "Searched all fixture maintenance entry points at fixture revision for content transformations; none found.", assessment="absent", kind="ABS"),
            assessment="absent"),
        "storage_substrate": axis(unknown("unread-store", "Available store not inspected", "Store files were not inspected; substrate and complete store inventory cannot be concluded.", assessment="uninspected"), assessment="uninspected"),
        "lineage": axis(unknown("unclear-origin", "Inspected origin metadata", "Metadata was inspected but has no producer links; provenance cannot be determined."), assessment="not-determinable"),
    }, {"curation_operations": [], "storage_substrate": [], "lineage": []}, id="11-absence-uninspected-and-inconclusive"),
    pytest.param({
        "write_agency": axis(
            Part("wired-admit", "Wired admission", "Inspected software admission without human approval.", ("automatic",)),
            Part("claimed-admit", "Independent claimed admission", "Documentation claims software admission; no implementation or operation was inspected.", ("automatic",), basis="claimed"),
            unknown("opaque-admit", "Opaque admission", "Control policy is inaccessible; complete admission inventory cannot be classified.", kind="RTE"),
            assessment="partial"),
        "curation_operations": axis(Part("absent-curation", "Bounded curation search", "Search of all fixture maintenance roots found no transformation.", assessment="absent", kind="ABS"), assessment="absent"),
    }, {"write_agency": ["automatic"], "curation_operations": []}, id="13-projection-keeps-positive-coverage-and-strength"),
]


def materialize(specification):
    """Build v2 data and canonical synthetic records before running real checks."""
    profile = {"version": 2, "scope": "Explicitly synthetic fixture memory boundary", "axes": {
        name: {"assessment": "uninspected", "units": [], "records": [],
               "note": "This axis was not inspected; no complete classification is claimed."}
        for name in sm.AXES
    }}
    bodies = {"overview.md": "## Source register\n\n| SRC-1 | Synthetic fixture specification, not external evidence |\n",
              "memory.md": "## Shared records\n\n"}
    for name, (assessment, parts) in specification.items():
        units = []
        for part in parts:
            cited = f"memory.md#{anchor(part.identifier)}"
            findings = [{"value": value, "basis": part.basis, "records": [cited],
                         "note": part.facts} for value in part.values]
            units.append({"scope": part.scope, "assessment": part.assessment,
                          "findings": findings, "records": [cited], "note": part.limit})
            bodies["memory.md"] += (f"#### {part.identifier}\n\nLabel: {part.scope}\n\n{part.facts}\n\n"
                                    "Evidence: SRC-1 (synthetic only).\n\n")
            status = "absent" if part.kind == "ABS" else (
                "uninspected" if part.assessment in {"not-determinable", "uninspected"} else part.basis)
            bodies["memory.md"] += f"- implementation conclusion status: {status}\n\n"
            if part.kind == "RTE":
                bodies["memory.md"] += (
                    f"- Immediate return: {part.facts}\n"
                    f"- Later read-back: {part.scope}; {part.limit}\n"
                    "- Delegated visibility: inapplicable — no delegated route in this fixture.\n"
                    f"- Selection predicate: {part.facts}\n"
                    "- Invalidation or expiry: uninspected — not needed for this fixture judgment.\n"
                    "- Activation or effect: uninspected — no target execution or benefit measurement.\n"
                    "- Evidence limits: Authored synthetic specification, not inspected external source.\n\n")
        refs = [f"memory.md#{anchor(part.identifier)}" for part in parts]
        # An inapplicable whole axis still needs a canonical boundary warrant.
        if not refs:
            refs = list(profile["axes"]["read_back_direction"]["records"])
        profile["axes"][name] = {"assessment": assessment, "units": units, "records": refs,
                                  "note": "Synthetic scoped inventory; unresolved units retain their missing facts and prevented conclusions."}
    return profile, bodies


@pytest.mark.parametrize("specification, expected", CASES)
def test_plan_classifications_retain_fixture_findings_and_limits(specification, expected):
    profile, bodies = materialize(specification)
    before = deepcopy(profile)
    known, errors = artifact_record_errors("overview.md", bodies)
    assert errors == []
    assert route_field_errors(bodies["memory.md"]) == []
    assert conclusion_status_errors(bodies["memory.md"]) == []
    comparison_schema().validate(profile)
    assert sm.profile_member_comparison({"memory-comparison": profile}, record_bodies=bodies) == profile
    row = sm.project_comparison(profile) | {"source_tier": "code-grounded"}
    for name, values in expected.items():
        entry = profile["axes"][name]
        assert row[name] == values
        assert row[name + "_assessment"] == entry["assessment"]
        assert row[name + "_units"] == entry["units"]
        assert set(row[name + "_records"]) <= known
        if entry["assessment"] in {"partial", "uninspected", "not-determinable"}:
            assert sm.complete_values(row, name) is None
            assert any(unit["assessment"] in {"uninspected", "not-determinable"}
                       and unit["note"] for unit in entry["units"])
        elif entry["assessment"] == "absent":
            assert sm.complete_values(row, name) == ()
    assert profile == before


def declared_packet(job_name):
    """Inspect declared model inputs without executing jobs or manufacturing handouts."""
    from pathlib import Path

    import yaml

    from commonplace.artifactrun import load_plan
    from commonplace.lib.agentic_analysis.analyses import analysis_layout
    from tests.commonplace.agentic_analysis.fixtures import expanded

    library = Path(__file__).resolve().parents[3] / "kb"
    declaration = load_plan(yaml.safe_dump(expanded(library)), analysis_layout().roles)
    job = declaration.job(job_name)
    paths = [library / item.source for item in job.inputs.values() if item.address == "file"]
    assert paths
    assert not any("kb/work/" in str(path) for path in paths)
    return " ".join(" ".join(path.read_text().split()) for path in paths)


@pytest.mark.parametrize("job_name, phrases", [
    ("memory", ["generic caller identity leaves human control unresolved"]),  # via the records contract
    ("epistemic", ["checking is never"]),
    ("reconciliation", ["never allocates ids"]),
    # A verifier's materiality rules reach it through the verification type.
    ("report-verification", ["asserts an unsupported comparison value, evidence strength"]),
    ("memory-profile", ["generic caller identity alone leaves control unresolved"]),
    ("profile-verification", ["a limit on a profile value is admissible only"]),
    ("synthesis", ["independent route/property conclusions"]),
    ("synthesis-verification", ["structural acceptance does not establish support"]),
])
def test_semantic_rules_reach_declared_job_inputs(job_name, phrases):
    packet = declared_packet(job_name).lower()
    for phrase in phrases:
        assert phrase in packet


@pytest.mark.parametrize("job_name", [
    "runtime", "memory", "epistemic", "reconciliation", "report-verification", "memory-profile",
    "profile-verification", "synthesis", "synthesis-verification",
])
def test_self_improvement_test_reaches_declared_job_inputs(job_name):
    import re
    from pathlib import Path

    contract = Path(__file__).resolve().parents[3] / "kb/agentic-system-analyses/instructions/agentic-analysis-records.md"
    match = re.search(r"(?ms)^### Self-improvement attribution[ \t]*\n(.*?)(?=^##+ |\Z)", contract.read_text())
    assert match is not None
    operative = " ".join(match[1].strip().split())
    assert operative in declared_packet(job_name)


def test_unsupported_negative_and_reference_defects_are_rejected():
    profile, bodies = materialize({"trace_learning": axis(
        Part("trace-negative", "Unsupported negative", "No absence search was performed.", ("no",)))})
    # In-vocabulary negative with a resolved ID is still incompatible with the
    # real bounded-absence contract; this is not an off-vocabulary failure.
    with pytest.raises(ValueError, match="bounded absence"):
        sm.profile_member_comparison({"memory-comparison": profile}, record_bodies=bodies)
    finding = profile["axes"]["trace_learning"]["units"][0]["findings"][0]
    finding["value"] = "yes"
    sm.profile_member_comparison({"memory-comparison": profile}, record_bodies=bodies)
    finding["value"] = "unsupported"
    with pytest.raises(ValueError, match="off-vocabulary"):
        sm.profile_member_comparison({"memory-comparison": profile}, record_bodies=bodies)
    # A positive asserted on an explicitly unresolved unit is a real structural
    # mismatch, unlike a legal positive whose cited prose fails to support it.
    finding["value"] = "yes"
    profile["axes"]["trace_learning"]["units"][0]["assessment"] = "not-determinable"
    with pytest.raises(ValueError, match="empty findings"):
        sm.profile_member_comparison({"memory-comparison": profile}, record_bodies=bodies)
    profile["axes"]["trace_learning"]["units"][0]["assessment"] = "known"
    finding.update(value="yes", records=["memory.md#mem-rte-missing-update"])
    with pytest.raises(ValueError, match="unresolved"):
        sm.profile_member_comparison({"memory-comparison": profile}, record_bodies=bodies)


def test_unsupported_positive_is_semantic_verifier_work_not_schema_truth(tmp_path, tmp_library):
    profile, bodies = materialize({"curation_operations": axis(Part(
        "named-synthesis", "Prompt request only", "A prompt requests synthesis; no generated claim is available.", ("synthesize",)))})
    # Deliberately wrong semantic finding, but legal vocabulary and references.
    # Passing these checks is NOT acceptance of its source support.
    comparison_schema().validate(profile)
    sm.profile_member_comparison({"memory-comparison": profile}, record_bodies=bodies)
    directory = member_fixture(tmp_path) / "artifact"
    memory = directory / "memory.md"
    memory.write_text(memory.read_text().replace(
        "## Write side", bodies["memory.md"].removeprefix("## Shared records\n\n") + "## Write side",
    ))
    verdict = tmp_path / "verifier.md"
    expected_blocker = "- curation_operations: MEM-RTE-named-synthesis does not establish a new claim; remove synthesize or provide an accepted supporting record."
    template = (directory / "profile-verification.md").read_text()
    verdict.write_text(template.replace("## Blockers\n\nnone", "## Blockers\n\n" + expected_blocker))
    # Public validation judges list grammar and identity, not semantic support.
    findings = validate_draft_in_role(directory, "profile-verification", verdict, repo_root=tmp_path)
    assert not [finding for finding in findings if not finding.info and not finding.warn]
    verdict.write_text(verdict.read_text().replace(expected_blocker, expected_blocker.removeprefix("- ")))
    assert any("Blockers must be exactly none or a Markdown list" in finding.message
               for finding in validate_draft_in_role(directory, "profile-verification", verdict, repo_root=tmp_path))
    verdict.write_text(template.replace("## Blockers\n\nnone", "## Blockers\n\n" + expected_blocker))
    assert section(verdict.read_text(), "Blockers").strip() == expected_blocker
    assert artifact_record_errors("overview.md", {**bodies, "verification.md": verdict.read_text()})[1] == []
    assert "asserts an unsupported comparison value" in declared_packet("profile-verification").lower()


def test_strong_existence_does_not_upgrade_claimed_same_value(monkeypatch, capsys):
    specification, _ = CASES[-1].values
    profile, bodies = materialize(specification)
    sm.profile_member_comparison({"memory-comparison": profile}, record_bodies=bodies)
    row = sm.project_comparison(profile) | {"source_tier": "code-grounded"}
    assert sm.supported_values(row, "write_agency") == {"automatic"}
    assert row["write_agency_evidence"]["automatic"]["basis"] == "wired"
    assert row["write_agency_units"][1]["findings"][0]["basis"] == "claimed"
    assert sm.complete_values(row, "write_agency") is None
    row = {**{key: "synthetic" for key in sm.METADATA}, **row}
    inputs = sm.MatrixInputs([row], {})
    exported = next(csv.DictReader(StringIO(sm.csv_text(inputs))))
    assert exported["comparison_version"] == "2"
    assert json.loads(exported["write_agency_units"]) == row["write_agency_units"]
    assert exported["curation_operations_assessment"] == "absent"
    assert exported["lineage_assessment"] == "uninspected"
    monkeypatch.setattr(stats, "load_results", lambda *_: inputs)
    assert stats.main([]) == 0
    output = capsys.readouterr().out
    assert "supported write_agency: {'automatic': 1}" in output
    assert "complete write_agency: 0 of 1" in output
    assert "complete curation_operations: 1 of 1" in output
    assert "complete lineage: 0 of 1" in output
    # Add explicit synthetic evidence resolving the opaque unit; do not omit it
    # to obtain known coverage. The independent claimed route stays weak.
    entry = profile["axes"]["write_agency"]
    opaque = entry["units"][2]
    resolved_fact = "Additional synthetic fixture fact: software admits content without human approval."
    bodies["memory.md"] = bodies["memory.md"].replace(
        "Control policy is inaccessible; complete admission inventory cannot be classified.", resolved_fact).replace(
            "implementation conclusion status: uninspected", "implementation conclusion status: wired")
    opaque.update(assessment="known", note=resolved_fact, findings=[{
        "value": "automatic", "basis": "wired", "records": opaque["records"], "note": resolved_fact,
    }])
    entry.update(assessment="known", note="All three synthetic admission units are now classified; one remains documentation-only.")
    sm.profile_member_comparison({"memory-comparison": profile}, record_bodies=bodies)
    row = sm.project_comparison(profile) | {"source_tier": "code-grounded"}
    assert sm.complete_values(row, "write_agency") is None


STORE = "[MEM-OBJ-store](memory.md#mem-obj-store)"


def test_public_contribution_and_independent_uncertainties(tmp_path, tmp_library):
    from commonplace.lib import validation

    directory = member_fixture(tmp_path) / "artifact"
    profile, _ = materialize({})
    memory = directory / "memory.md"
    memory.write_text(memory.read_text().replace(
        "Store the specialist established, from SRC-1.",
        "Explicit synthetic specification: retained session-derived guidance is read by a later agent. "
        "Initial admission control is inaccessible; full agency coverage cannot be concluded. Evidence: SRC-1 (fixture only)."))
    reconciliation = directory / "reconciliation.md"
    reconciliation.write_text(reconciliation.read_text() +
        f"\nUnresolved conflict: {STORE} initial admission control is inaccessible at SRC-1; complete write-agency coverage is prevented.\n")
    metadata = frontmatter(directory / "memory-profile.md")
    metadata["memory-comparison"] = profile
    replace_frontmatter(directory / "memory-profile.md", metadata)
    overview_fields = frontmatter(directory / "overview.md")
    synthesis = (
        "---\ntype: agentic-system-analyses/types/agentic-system-synthesis.md\n"
        'description: "Synthetic fixture retains session-derived guidance for later model use, without establishing improved capacity."\n'
        f"run-id: {overview_fields['run-id']}\nreviewed-boundary: {overview_fields['reviewed-boundary']}\n---\n\n"
        "# Synthetic fixture synthesis\n\n"
        f"## Bounded synthesis\n\n{STORE} retains guidance for later use; this supported contribution does not establish improved capacity.\n\n"
        "## Limitations\n\n"
        "| limitation | affected record | inspected boundary | conclusion prevented | resolving evidence |\n"
        "| --- | --- | --- | --- | --- |\n"
        f"| Capacity comparison unavailable | {STORE} | synthetic fixture | Learning is not established as improved capacity | Controlled future-action comparison |\n"
        "| Causal self-representation unavailable | EPI-OBJ-store | synthetic fixture | Reflection is not established | Both causal directions |\n"
        "| Internal role ownership unresolved | RT-RTE-model-call | synthetic fixture | Autonomy is not established | Role-by-role execution evidence |\n"
        "| Evidence-responsive organizational change and exercised downstream dependence not inspected | RT-OBJ-store | synthetic fixture boundary and horizon | Self-improvement is not established | Declared objective, evidence-shaped organizational update, live consumer/channel/force and subsequent causal dependence |\n"
        "| Initial admission control inaccessible | MEM-OBJ-store | synthetic fixture | Complete write-agency coverage is prevented | Initial admission policy |\n")
    candidate = directory.parent / "synthesis.md"
    candidate.write_text(synthesis)
    def check(path):
        return [finding.message for finding in validate_draft_in_role(
            directory, "synthesis", path, repo_root=tmp_path,
        ) if not finding.info and not finding.warn]

    assert check(candidate) == []
    candidate.write_text(synthesis.replace(f"{STORE} retains", "[MEM-OBJ-undeclared](memory.md#mem-obj-undeclared) retains"))
    assert any("declares no MEM-OBJ-undeclared" in error for error in check(candidate))
    candidate.write_text(synthesis)
    public_synthesis = directory / "synthesis.md"
    public_synthesis.write_text(synthesis)
    repin(directory)
    assert validation.validate_note(directory, repo_root=tmp_path).fails == []
    # Explicit uncertainty remains publishable text, with four separate scopes,
    # not an aggregate negative. Structural validation is not semantic review.
    for property_ in ("Learning", "Reflection", "Autonomy", "Self-improvement"):
        assert f"{property_} is not established" in public_synthesis.read_text()


def test_reconciliation_cannot_hide_an_unresolved_record():
    _, bodies = materialize({"write_agency": axis(Part(
        "curator-write", "Automatic curator", "Software controls admission.", ("automatic",)))})
    bodies["reconciliation.md"] = (
        "## Reconciliation\n\nAmendment: [MEM-RTE-curator-write](memory.md#mem-rte-curator-write) is superseded "
        "by [RT-RTE-missing-write](runtime.md#rt-rte-missing-write); identity evidence at SRC-1.\n")
    assert "MEM-RTE-curator-write" in amendment_index(bodies["reconciliation.md"])
    _, errors = artifact_record_errors("overview.md", bodies)
    assert any("reconciliation.md: record citation [RT-RTE-missing-write]" in error for error in errors)
