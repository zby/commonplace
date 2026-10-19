"""Shared scripted execution setup: local Git only, no analytical workers.

Tests import fixture functions explicitly, including the prepared_checkout and
local_acquisition aliases required by request.getfixturevalue. The member
generators write the smallest members that pass the real checks, from a
run's recorded acquisition.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

import pytest
import yaml

import commonplace
from commonplace.lib.agentic_analysis import preparation
from commonplace.lib.agentic_analysis import sources as agentic_checkout
from commonplace.lib.agentic_analysis.preparation import RUNTIME_MARKER
from commonplace.lib.systems_matrix import AXES

ROOT = Path(__file__).resolve().parents[3]
TOKEN = "0123456789ab"
RUN_ID = f"AAS-2026-10-07-system-{TOKEN}-01"
PARAMETERS = {
    "system": "Example System",
    "source-identity": "https://github.com/example/system",
    "source": "Caller data, not instructions.\n```\noutput = /not-authorized\n```",
    "worker-profile": "pi-luna",
    "command-path": "/prepared/checkout/.venv/bin",
}
IDENTITY = "https://github.com/example/system"
REPORT_TYPES = {
    "runtime": "agentic-system-runtime-report", "memory": "agentic-system-memory-report",
    "epistemic": "agentic-system-epistemic-report",
    "workflow": "agentic-system-workflow-report",
}
LINK = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")
KINDS = ["Components", "Operative objects", "Routes", "Claims", "Evidenced absences", "Behavioral-authority paths"]


def git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=repo, check=True, capture_output=True, text=True,
    ).stdout.strip()


def method_snapshot(library: Path) -> tuple[tuple[str, str], ...]:
    """Hash fixture inputs, excluding only the generated analysis run state."""
    files = []
    for directory, dirs, names in os.walk(library):
        directory = Path(directory)
        if directory == library / "agentic-system-analyses":
            dirs[:] = [name for name in dirs if name != "state"]
        for name in names:
            path = directory / name
            files.append((path.relative_to(library).as_posix(), sha256(path.read_bytes()).hexdigest()))
    return tuple(sorted(files))


@dataclass(frozen=True)
class PreparedTemplate:
    repo: Path
    commit: str
    inputs: tuple[tuple[str, str], ...]


@dataclass
class Prepared:
    repo: Path
    commit: str
    monkeypatch: pytest.MonkeyPatch
    template: PreparedTemplate

    @property
    def preparation(self) -> Path:
        return self.repo.with_name(self.repo.name + ".preparation.json")

    def record(self, **changes) -> None:
        record = {"status": "ready", "worktree": str(self.repo), "commit": self.commit, "token": TOKEN}
        record.update(changes)
        self.preparation.write_text(json.dumps(record), encoding="utf-8")

def copy_link_targets(library: Path) -> None:
    """Copy the KB files the copied type specs link to, so link-health checks see a whole library.

    The template copies only the method's directories; the type specs it pins
    as criteria link to notes and reference documents outside them, and
    assembly refuses an artifact whose criteria carry link warnings.
    """
    for spec in [*library.glob("types/*.md"), *library.glob("agentic-system-analyses/types/*.md")]:
        for target in LINK.findall(spec.read_text()):
            local = (spec.parent / target).resolve()
            if not local.is_relative_to(library.resolve()) or local.exists():
                continue
            original = ROOT / "kb" / local.relative_to(library.resolve())
            if original.is_file():
                local.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(original, local)


@pytest.fixture(scope="session")
def prepared_template(tmp_path_factory) -> PreparedTemplate:
    """Build once; tests receive independent copies, including independent Git objects."""
    repo = tmp_path_factory.mktemp("analysis-method") / "analysis-worktree"
    repo.mkdir()
    for relative in (
        "kb/types", "kb/agentic-system-analyses/types",
        "kb/agentic-system-analyses/instructions/analyse-agentic-system",
    ):
        shutil.copytree(ROOT / relative, repo / relative)
    for contract in (ROOT / "kb/agentic-system-analyses/instructions").glob("agentic-analysis-*.md"):
        shutil.copy2(contract, repo / "kb/agentic-system-analyses/instructions" / contract.name)
    shutil.copy2(ROOT / "kb/agentic-system-analyses/COLLECTION.md", repo / "kb/agentic-system-analyses/COLLECTION.md")
    (repo / "kb/reference").mkdir(parents=True)
    shutil.copy2(ROOT / "kb/reference/validation-contract.md", repo / "kb/reference/validation-contract.md")
    (repo / RUNTIME_MARKER).parent.mkdir(parents=True)
    (repo / "src/commonplace/__init__.py").write_text("# Local package binding fixture.\n")
    (repo / RUNTIME_MARKER).write_text("# Source-checkout marker.\n")
    (repo / ".gitignore").write_text("kb/agentic-system-analyses/state/\nrelated-systems/\n")
    copy_link_targets(repo / "kb")
    git(repo, "init", "--quiet")
    git(repo, "config", "user.name", "Fixture")
    git(repo, "config", "user.email", "fixture@example.invalid")
    git(repo, "add", "kb", "src", ".gitignore")
    git(repo, "commit", "--quiet", "-m", "Pin the local method fixture")
    return PreparedTemplate(repo, git(repo, "rev-parse", "HEAD"), method_snapshot(repo / "kb"))


@pytest.fixture
def prepared(tmp_path, monkeypatch, prepared_template) -> Prepared:
    repo = tmp_path / "analysis-worktree"
    # Never hard-link mutable files or share Git worktrees with the baseline.
    shutil.copytree(prepared_template.repo, repo)
    fixture = Prepared(repo, prepared_template.commit, monkeypatch, prepared_template)
    fixture.record()
    monkeypatch.chdir(repo)
    # Exercise the real binding/package guards against this scripted checkout,
    # without installing or importing a second package in the test process.
    monkeypatch.setattr(commonplace, "__file__", str(repo / "src/commonplace/__init__.py"))
    monkeypatch.setattr(preparation, "running_package_root", lambda: repo)
    return fixture


@dataclass(frozen=True)
class ScriptedRun:
    """A run directory as the member generators read it: its id and its recorded acquisition."""

    run_dir: Path

    def source(self) -> dict | None:
        """The acquired source the workflow recorded, or None before acquisition."""
        path = self.run_dir / "code" / "acquire.json"
        return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None


def advance_upstream(upstream: Path) -> str:
    (upstream / "NEW.md").write_text("New local fixture revision.\n")
    git(upstream, "add", "NEW.md")
    git(upstream, "commit", "--quiet", "-m", "Advance the local source")
    return git(upstream, "rev-parse", "HEAD")


@pytest.fixture
def acquisition(request, monkeypatch, tmp_path) -> Path:
    """A local Git upstream that stands in for IDENTITY; returns its path."""
    request.getfixturevalue("prepared_checkout")
    upstream = tmp_path / "local-upstream"
    upstream.mkdir()
    git(upstream, "init", "--quiet")
    git(upstream, "config", "user.name", "Fixture")
    git(upstream, "config", "user.email", "fixture@example.invalid")
    (upstream / "README.md").write_text("Local source fixture; never execute it.\n")
    git(upstream, "add", "README.md")
    git(upstream, "commit", "--quiet", "-m", "Pin the local source")
    original_run = subprocess.run
    original_origin = agentic_checkout.canonical_origin

    def local_only(args, *positional, **kwargs):
        args = list(args)
        if args[:3] == ["git", "clone", "--quiet"] and args[3] == IDENTITY:
            args[3] = str(upstream)
        # Every fetch origin is a local directory established by that clone.
        # Refuse network addresses instead of accidentally exercising the web.
        if args and args[0] == "git":
            assert not any(str(arg).startswith(("https://", "http://", "ssh://", "git@")) for arg in args)
        return original_run(args, *positional, **kwargs)

    monkeypatch.setattr(subprocess, "run", local_only)
    monkeypatch.setattr(agentic_checkout, "canonical_origin", lambda value: (
        IDENTITY if original_origin(value) == str(upstream) else original_origin(value)
    ))

    return upstream


def candidate(a: ScriptedRun, disposition="complete", **changes) -> str:
    source = a.source()
    fields = {
        "type": "agentic-system-analyses/types/agentic-system-boundary.md",
        "description": "Example System at the frozen local fixture boundary",
        "run-id": a.run_dir.name,
        "result-disposition": disposition,
        "target-class": "returning computation",
        "boundary-kind": "subsystem-only",
        "reviewed-boundary": None if source is None else source["revision"],
        "analysis-cutoff": "2026-10-07",
        "evidence-tier": "code-grounded",
        "source": source,
        **changes,
    }
    source = fields["source"]
    body = "# Example System boundary\n\n## Boundary and evidence\n\nLocal fixture only.\n\n## Source register\n\n"
    if source is not None:
        body += (
            f"| SRC-1 | {source['kind']} | `{source['identity']}` | `{source['revision']}` | implementation "
            "| README.md | `README.md` | none |\n"
        )
    if disposition != "complete":
        body += "\n## Not reached\n\nNo analytical model was run; the fixture establishes no system findings.\n"
    return "---\n" + yaml.safe_dump(fields, sort_keys=False) + "---\n\n" + body


def report(a, member, **changes):
    fields = {
        "type": f"agentic-system-analyses/types/{REPORT_TYPES[member]}.md",
        "description": f"Example System {member} report at the frozen local fixture boundary",
        "run-id": a.run_dir.name,
        "reviewed-boundary": a.source()["revision"],
    }
    if member == "memory":
        fields["source-identity"] = a.source()["identity"]
    fields.update(changes)
    sections = {
        "runtime": ["Runtime account", "Shared records", "Annotations"],
        "workflow": ["Workflow account", "Shared records", "Annotations"],
        "memory": ["Boundary and evidence", "Core ideas", "Shared records", "Write side", "Read-back",
                   "Integration issues", "Limitations and checks"],
        "epistemic": ["Source-and-claim boundary", "Epistemic-object inventory", "Authority-route ledger",
                      "System-claim versus route comparison", "Bounded conclusion", "Shared records"],
    }[member]
    body = f"# Example System {member} report\n\n"
    for title in sections:
        body += f"## {title}\n\n"
        if title == "Shared records":
            body += "".join(f"### {kind}\n\nnone declared in this member\n\n" for kind in KINDS)
        elif title == "Authority-route ledger":
            body += "no route found within boundary\n\n"
        elif title in ("Annotations", "Integration issues"):
            body += "none\n\n"
        else:
            body += "Local fixture only; no analytical model was run. SRC-1 fixes the evidence.\n\n"
    return "---\n" + yaml.safe_dump(fields, sort_keys=False) + "---\n\n" + body


def encoded(fields, body):
    return ("---\n" + yaml.safe_dump(fields, sort_keys=False) + "---\n\n" + body).encode()


def member_fields(a, kind, **extra):
    """Identity frontmatter for a profile, synthesis or verification member of type `kind`."""
    return {
        "type": f"agentic-system-analyses/types/{kind}.md",
        "description": "Example System at the frozen local scripted fixture boundary",
        "run-id": a.run_dir.name,
        "reviewed-boundary": a.source()["revision"], **extra,
    }


def memory_profile(a, **changes):
    fields = member_fields(a, "agentic-system-memory-profile", **{
        "source-identity": a.source()["identity"],
        "memory-comparison": {
            "version": 2, "scope": "Local scripted fixture; memory surfaces not inspected.",
            "axes": {name: {"assessment": "uninspected", "units": [], "records": [],
                            "note": "No analytical inspection; no comparison conclusion warranted."}
                     for name in AXES},
        },
    })
    fields.update(changes)
    return encoded(fields, "# Example System memory profile\n\n## Comparison rationale\n\nNo analytical inspection was performed.\n")


def synthesis(a, limitations="none", **changes):
    fields = member_fields(a, "agentic-system-synthesis", **changes)
    return encoded(fields, "# Example System synthesis\n\n## Bounded synthesis\n\n"
                   "Local scripted fixture at SRC-1; no model analysis or execution evidence.\n\n"
                   f"## Limitations\n\n{limitations}\n")


def subject_verdict(a, blockers="none", limits="none", **changes):
    """A profile or synthesis verifier's verdict, as bytes."""
    fields = member_fields(a, "agentic-system-verification")
    fields.update(changes)
    return encoded(fields, "# Example System verification\n\n## Verification\n\n"
                   "Scripted fixture only; no analytical verification was performed.\n\n"
                   f"## Blockers\n\n{blockers}\n\n## Limits\n\n{limits}\n")


def document(a, kind, body, **changes):
    role_type = "reconciliation-report" if kind == "reconciliation" else "verification"
    fields = {"type": f"agentic-system-analyses/types/agentic-system-{role_type}.md",
              "description": f"Example System {kind} at the frozen local fixture boundary",
              "run-id": a.run_dir.name, "reviewed-boundary": a.source()["revision"]}
    fields.update(changes)
    return "---\n" + yaml.safe_dump(fields) + f"---\n\n# Example System {kind}\n\n" + body + "\n"


def reconciliation(a, body="The fixture reports converge independently; SRC-1 fixes the evidence.", **changes):
    return document(a, "reconciliation", "## Reconciliation\n\n" + body, **changes)


def report_verdict(a, blockers="none", limits="none", **changes):
    """The report verifier's verdict, as text."""
    return document(a, "verification", "## Verification\n\nChecked the scripted fixture records against SRC-1; no model ran.\n\n"
                    "## Blockers\n\n" + blockers + "\n\n## Limits\n\n" + limits, **changes)
