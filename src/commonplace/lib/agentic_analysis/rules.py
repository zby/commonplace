"""The analysis types' validation rules, registered with the validator.

Rules the analysis type specs and their schemas cannot express: record
declarations, which a correction keeps, and references, the source register, the epistemic ledger, artifact
member links, and the analysis artifact's cross-member relations, including
quotations resolved against the boundary's frozen source. Importing this
module registers them.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from commonplace.lib.agentic_analysis.analyses import RETAINED_ROOT, source_slug
from commonplace.lib.agentic_analysis.ledger import epistemic_ledger_errors
from commonplace.lib.agentic_analysis.records import (
    amendment_index,
    annotated_ids,
    artifact_declarations,
    artifact_record_findings,
    conclusion_status_errors,
    declared_ids,
    record_reference_errors,
    record_references,
    route_field_errors,
    source_register_ids,
    source_register_rows,
    value_amendments,
)
from commonplace.lib.directory_artifact import DirectoryArtifact
from commonplace.lib.directory_layout import Finding, Layout
from commonplace.lib.note_parser import (
    ParsedDocument,
    blank_fenced_code_blocks,
    section,
)
from commonplace.lib.quote_grounding import (
    FrozenGitObjects,
    frozen_source_pin,
    resolve_citations,
)
from commonplace.lib.quote_matching import (
    URL_RE,
    Citation,
    blank_quote_bodies,
    parse_blockquotes,
    parse_github_blob,
    ranged_prose_anchors,
)
from commonplace.lib.systems_matrix import validate_comparison
from commonplace.lib.validation import (
    CheckResults,
    ParsedNote,
    ValidationRun,
    declaration_grammar,
    directory_type_rule,
    resolve_local_link_target,
    type_rule,
    validate_quote_citations,
)

# The analysts' records keep their IDs for the life of the artifact: a
# correction rewrites a finding without changing what its record names.
declaration_grammar(
    "agentic-system-analyses/types/agentic-system-runtime-report.md",
    "agentic-system-analyses/types/agentic-system-memory-report.md",
    "agentic-system-analyses/types/agentic-system-epistemic-report.md",
)(declared_ids)


@type_rule("agentic-system-analyses/types/agentic-system-boundary.md")
def _agentic_boundary_register_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """The register's shape and identity are content, not invocation checks."""
    body = parsed.document.body
    rows = source_register_rows(body)
    errors = [
        f"source register: {row[0]} needs all eight columns the boundary type defines"
        for row in rows if len(row) != 8
    ]
    errors.extend(
        f"duplicate source declaration: {identifier}; keep one row per source ID "
        "and separate evidence layers and scopes within that row"
        for identifier, count in Counter(source_register_ids(body)).items() if count > 1
    )
    source = (parsed.document.frontmatter or {}).get("source")
    if isinstance(source, dict):
        expected = tuple(str(source.get(field) or "") for field in ("kind", "identity", "revision"))
        if not any(
            len(row) == 8 and tuple(cell.strip("`") for cell in row[1:4]) == expected
            for row in rows
        ):
            errors.append(
                "source register must declare the frozen source in a SRC-* row: "
                f"kind `{expected[0]}`, identity `{expected[1]}`, revision or capture `{expected[2]}`"
            )
    results.fails.extend(errors)
    if not errors:
        results.passes.append("source register: eight-column rows, unique IDs and frozen source checked")


@type_rule("agentic-system-analyses/types/agentic-system-reconciliation-report.md")
def _agentic_reconciliation_amendment_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:

    errors = [
        "value amendment: reconciliation states connections between reports and does "
        "not replace a record's value; describe the disagreement with both records and "
        "their evidence, or use `Amendment: <record citation> is superseded by <record citations>` for an "
        f"identity judgment: {line[:120]}"
        for line in value_amendments(parsed.document.body)
    ]
    results.fails.extend(errors)
    if not errors:
        results.passes.append("reconciliation amendments: only identity supersessions")


@type_rule("agentic-system-analyses/types/agentic-system-memory-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-runtime-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-epistemic-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-reconciliation-report.md")
def _agentic_evidence_and_references_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:

    field_errors = route_field_errors(parsed.document.body)
    results.fails.extend(field_errors)
    if not field_errors:
        results.passes.append("route fields: required labels and non-empty answers checked")
    status_errors = conclusion_status_errors(parsed.document.body)
    results.fails.extend(status_errors)
    if not status_errors:
        results.passes.append("conclusion status: labelled route fields and controlled values checked")
    validate_quote_citations(results, parsed.content)


@type_rule("agentic-system-analyses/types/agentic-system-boundary.md")
@type_rule("agentic-system-analyses/types/agentic-system-analysis-overview.md")
@type_rule("agentic-system-analyses/types/agentic-system-runtime-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-memory-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-epistemic-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-reconciliation-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-verification.md")
@type_rule("agentic-system-analyses/types/agentic-system-synthesis.md")
@type_rule("agentic-system-analyses/types/agentic-system-memory-profile.md")
def _record_reference_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """Record syntax and declarations one member shows alone.

    A member validated alone cannot resolve references the artifact declares
    elsewhere; the analysis artifact's directory rule resolves them across the
    members.
    """
    del run
    errors = record_reference_errors(parsed.document.body)
    results.fails.extend(errors)
    if not errors:
        results.passes.append("record references: declarations, labels and citation syntax checked")


def artifact_member_link_failures(path: Path, links: tuple[str, ...]) -> list[str]:
    """Links must survive moving a member into a retained artifact directory."""
    directory = path.resolve().parent
    return [
        f"artifact member link: {link} leaves the artifact directory and breaks once "
        "retained; name the file by path in a code span"
        for link in links
        if (target := resolve_local_link_target(path, link)) is not None
        and target.parent != directory
    ]


@type_rule("agentic-system-analyses/types/agentic-system-analysis-overview.md")
@type_rule("agentic-system-analyses/types/agentic-system-runtime-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-memory-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-epistemic-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-reconciliation-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-verification.md")
@type_rule("agentic-system-analyses/types/agentic-system-synthesis.md")
def _agentic_plain_source_anchor_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """Only quote attributions carry line ranges; prose anchors cite paths."""
    del run
    found = ranged_prose_anchors(parsed.content)
    for line, anchor in found:
        results.fails.append(
            f"source anchor at line {line}: {anchor} carries a line range; "
            "cite the path without a range, or quote the passage"
        )
    if not found:
        results.passes.append("source anchors: prose anchors cite paths without ranges")


@type_rule("agentic-system-analyses/types/agentic-system-analysis-overview.md")
@type_rule("agentic-system-analyses/types/agentic-system-runtime-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-memory-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-epistemic-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-reconciliation-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-verification.md")
@type_rule("agentic-system-analyses/types/agentic-system-synthesis.md")
@type_rule("agentic-system-analyses/types/agentic-system-memory-profile.md")
@type_rule("agentic-system-analyses/types/agentic-system-boundary.md")
def _artifact_member_link_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """Relative links stay inside the artifact directory, which moves on retention."""
    del run
    failures = artifact_member_link_failures(parsed.path, parsed.document.links)
    results.fails.extend(failures)
    if not failures:
        results.passes.append("artifact member links: relative links stay inside the artifact directory")


@type_rule("agentic-system-analyses/types/agentic-system-runtime-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-memory-report.md")
@type_rule("agentic-system-analyses/types/agentic-system-epistemic-report.md")
def _record_prefix_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """A report declares records only under its type's ``record-prefix``."""
    assert parsed.profile.type_doc_path is not None
    prefix = run.load_frontmatter(parsed.profile.type_doc_path).data.get("record-prefix")
    if not isinstance(prefix, str) or not prefix:
        results.fails.append(f"record declarations: {parsed.profile.type_name} declares no record-prefix")
        return
    foreign = [identifier for identifier in declared_ids(parsed.document.body)
               if not identifier.startswith(prefix)]
    if foreign:
        results.fails.append(
            f"record declarations: this report declares only {prefix} records: "
            + ", ".join(foreign)
            + "; keep supplied IDs unchanged in references and annotations"
        )
    else:
        results.passes.append(f"record declarations: every declaration uses {prefix}")


@type_rule("agentic-system-analyses/types/agentic-system-memory-report.md")
def _memory_report_pending_check_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:

    checks = blank_fenced_code_blocks(section(parsed.document.body, "Limitations and checks"))
    if re.search(r"(?im)^[ \t]*(?:\*\*)?Validation(?:\*\*)?:[ \t]*(?:`|\*\*)?pending\b", checks):
        results.fails.append("memory checks: a report cannot retain 'Validation: pending'")


@type_rule("agentic-system-analyses/types/agentic-system-epistemic-report.md")
def _epistemic_ledger_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:

    errors = epistemic_ledger_errors(parsed.document.body)
    results.fails.extend(errors)
    if not errors:
        results.passes.append("epistemic ledger: table/record syntax and controlled function/status checked")


@type_rule("agentic-system-analyses/types/agentic-system-memory-profile.md")
def _memory_profile_local_rule(
    results: CheckResults, parsed: ParsedNote, *, run: ValidationRun
) -> None:
    """The profile's own content; its references resolve in the artifact rule."""
    if re.search(r"(?m)^> ?", parsed.document.body):
        results.fails.append("memory profile cannot add source quotations")
    if declared_ids(parsed.document.body) or annotated_ids(parsed.document.body):
        results.fails.append("memory profile cannot declare or annotate records")



@directory_type_rule("agentic-system-analyses/types/agentic-system-analysis-set.md")
def validate_analysis_artifact(artifact: DirectoryArtifact, *, layout: Layout | None, run: ValidationRun) -> list[Finding]:
    """Relations the layout names but code must compute, over the members present."""
    if layout is None:
        return [Finding(None, "the analysis artifact type must declare a layout")]
    documents = {
        role.name: artifact.members[role.path].document
        for role in layout.roles.values() if role.path in artifact.members
    }
    findings = []
    pinned = artifact.manifest.get("members")
    if isinstance(pinned, dict):
        findings += [Finding(None, f"manifest: member {name} is not pinned")
                     for name in sorted(set(artifact.members) - set(pinned))]

    bodies = {layout.path(name): document.body for name, document in documents.items()}
    cites = {role.path: [layout.path(cited) for cited in role.cites] for role in layout.roles.values()}
    sources = layout.path("boundary")
    _, record_findings = artifact_record_findings(sources, bodies, cites=cites)
    for name, message, repair in record_findings:
        role = layout.role_at(name) if name else None
        findings.append(Finding(role.name if role else None, message, repair=repair))

    overview = documents.get("overview")
    reconciliation = documents.get("reconciliation")
    index = amendment_index(reconciliation.body) if reconciliation is not None else None
    if index is not None and overview is not None and index not in overview.body.splitlines():
        findings.append(Finding("overview", "overview amendment index does not match reconciliation"))
    if overview is not None:
        links = {link.split('#', 1)[0].removeprefix('./') for link in overview.links}
        for name in documents:
            if name != "overview" and layout.path(name) not in links:
                findings.append(Finding("overview", f"{layout.path('overview')}: missing member link to {layout.path(name)}",
                                        repair="link every present member from the overview's Members section"))

    findings += _artifact_quotation_findings(artifact, layout, documents, run=run)
    findings += _verification_findings(layout, documents)

    profile = documents.get("memory-profile")
    if profile is not None:
        declared = artifact_declarations(sources, bodies)
        scope = {identifier: cited for cited in cites[layout.path("memory-profile")]
                 for identifier in declared.get(cited, ())}
        try:
            validate_comparison((profile.frontmatter or {}).get("memory-comparison"), known_ids=scope)
        except ValueError as exc:
            findings.append(Finding("memory-profile", f"{layout.path('memory-profile')}: {exc}"))

    if artifact.path.parent == run.repo_root / RETAINED_ROOT:
        memory = documents.get("memory")
        if memory is None or overview is None:
            findings.append(Finding(None, "current analysis must be complete"))
        else:
            identity = (memory.frontmatter or {}).get("source-identity", "")
            if artifact.path.name != source_slug(identity, (overview.frontmatter or {}).get("system", "")):
                findings.append(Finding(None, "current directory name does not match its source"))
    return findings


def _verification_findings(layout: Layout, documents: dict[str, ParsedDocument]) -> list[Finding]:
    """List grammar and carried limits; meaning remains review."""

    findings = []
    synthesis = documents.get("synthesis")
    limitations = record_references(section(synthesis.body, "Limitations")) if synthesis else set()
    for name in ("report-verification", "profile-verification", "synthesis-verification"):
        document = documents.get(name)
        if document is None:
            continue
        path = layout.path(name)
        for title in ("Blockers", "Limits"):
            text = section(document.body, title).strip()
            if text == "none":
                continue
            lines = [line for line in text.splitlines() if line.strip()]
            valid = lines and lines[0].startswith("- ") and all(
                line.startswith(("- ", " ", "\t")) for line in lines
            )
            if not valid:
                findings.append(Finding(name, f"{path}: {title} must be exactly none or a Markdown list",
                                        repair=f"write none or one '- ' entry per {title.lower()} finding; indent continuation lines"))
                continue
            entries = re.split(r"(?m)^- ", text)[1:]
            if title == "Blockers" and name == "report-verification":
                for entry in entries:
                    if not re.match(r"(?:runtime|memory|epistemic|reconciliation): +\S", entry):
                        findings.append(Finding(name, f"{path}: report blocker has no report addressee",
                                                repair="start each blocker with runtime:, memory:, epistemic: or reconciliation: and its finding"))
            if title == "Limits" and synthesis is not None:
                for entry in entries:
                    cited = record_references(entry)
                    if cited and not cited & limitations:
                        findings.append(Finding("synthesis", f"{layout.path('synthesis')}: limit not carried: "
                                                f"Limitations names none of {', '.join(sorted(cited))} "
                                                f"for the limit {path} declares: {entry.splitlines()[0][:100]}",
                                                repair="carry the named limit, citing its affected records, into synthesis Limitations"))
    return findings


def _artifact_quotation_findings(
    artifact: DirectoryArtifact, layout: Layout, documents: dict[str, ParsedDocument],
    *, run: ValidationRun,
) -> list[Finding]:
    """Every member's quotations resolve against the boundary's frozen source.

    Pinned bytes absent from this machine leave the quotations unverified,
    reported once per member as information.
    """
    boundary = documents.get("boundary")
    source = (boundary.frontmatter or {}).get("source") if boundary is not None else None
    bounded = run.criteria is not None
    authorized = not bounded or (isinstance(source, dict) and source == run.frozen_source)
    complete_source = isinstance(source, dict) and all(
        isinstance(source.get(key), str) and source[key] for key in ("identity", "revision", "path")
    )
    pin = frozen_source_pin(source) if complete_source and authorized else None
    if bounded and pin is not None and source.get("kind") == "git":
        pin = FrozenGitObjects(source)
    findings = []
    if bounded and pin is None and any(
        "github.com/" in match.group() and "/blob/" in match.group()
        for document in documents.values() for match in URL_RE.finditer(document.body)
    ):
        findings.append(Finding("boundary", "source anchors require authorized frozen source inspection"))
    if bounded and isinstance(source, dict) and not authorized:
        findings.append(Finding("boundary", "frozen source inspection requires the exact boundary source context"))
    if bounded and pin is not None:
        if source.get("kind") not in {"git", "capture"} or not Path(str(source.get("path", ""))).is_absolute():
            return [Finding("boundary", "frozen source needs a git/capture kind and absolute path")]
        missing = pin.missing()
        if missing is not None:
            findings.append(Finding("boundary", f"frozen source unavailable: {missing}"))
        for name, document in documents.items():
            if source.get("kind") == "git":
                for match in URL_RE.finditer(blank_quote_bodies(document.body)):
                    url = match.group().rstrip(".,;")
                    try:
                        blob = parse_github_blob(url)
                        if blob is None:
                            continue
                        citation = Citation("", url, blob.revision)
                        error = pin.attribution_error(citation)
                        found = pin.read(citation, text=False) if error is None else None
                        error = error or (found.error or found.missing if found is not None else None)
                        if error:
                            findings.append(Finding(name, f"source citation: {error}: {url}"))
                    except ValueError as exc:
                        findings.append(Finding(name, f"source citation: {exc}"))
            else:
                # A GitHub blob citation cannot be established by a capture.
                for match in URL_RE.finditer(document.body):
                    url = match.group().rstrip(".,;")
                    try:
                        if parse_github_blob(url) is not None:
                            findings.append(Finding(name, "GitHub source anchor cannot be verified against a capture"))
                    except ValueError as exc:
                        findings.append(Finding(name, f"source citation: {exc}"))
    for role in layout.roles.values():
        if role.name not in documents:
            continue
        citations = parse_blockquotes(artifact.members[role.path].content.decode("utf-8"))
        if not citations:
            continue
        if pin is None:
            findings.append(Finding(role.name, f"{role.path}: quotations need the boundary's frozen source"))
            continue
        unverified = []
        for resolution in resolve_citations(citations, pin, kind="code"):
            if resolution.status == "mismatch":
                findings.append(Finding(role.name, f"{role.path}: quote-anchored citation at line "
                                                   f"{resolution.citation.line}: {resolution.detail}"))
            elif resolution.status == "unverified":
                unverified.append(resolution)
        if unverified:
            findings.append(Finding(role.name, f"{role.path}: {len(unverified)} quotations unverified, "
                                               f"{unverified[0].detail}", info=not bounded,
                                    repair="make the boundary's pinned source bytes available and check again"))
    return findings
