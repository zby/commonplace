"""A toy artifact type, a plan over it, and a scripted coordinator.

The toy plan mirrors the analysis mapping in
kb/work/workflow-requirements/analysis-workflow-as-job-set.md:

| Toy job | Analysis role | Kind |
|---|---|---|
| brief, check-brief | boundary and its check; carries the disposition | model, code |
| report, check-report | an analyst report (`R`, `check-R` in the scenarios) | model, code |
| other, check-other | a second analyst; its check has the report as input | model, code |
| summary, check-summary | reconcile | model, code |
| verification, apply-verification | verify-reports and its apply job (`V`) | model, code |
| digest, check-digest | profile, gated on the verification's acceptances | model, code |
| assemble | assemble, gated on coverage | code |

Nothing here runs a model. `Coordinator` writes the files a worker would
write at the hand-out paths, each primary output as a member of its role's
toy type, and reports attempt results. The checks and the verdict
application are the engine's standard handlers on real validation: a body
containing REFUSE fails every member schema, `Coordinator.forbid` edits the
report's schema (a pinned criterion), the other report repeats the report's
`claim` as a layout identity field, and verdicts follow the verification
protocol (`NO_BLOCKERS`, `blocking`).

Semantics these tests rely on, each now stated in the workshop documents:

- `RunStatus.handouts` lists the attempts opened by that invocation;
  `open_attempts` lists every attempt still open.
- The upstream-wait decision: a ready job is not run or handed out while a
  producer of one of its inputs is ready or has an open attempt. A member's
  producers are the job that fills its role and every job that judges it.
  Without it, a report correction makes the summary and the verifier ready
  together and the verifier runs against the stale summary. It also lets
  `assemble` wait for the run to settle with optional inputs only, whatever
  the disposition.
- Requirement 4's current-subject rule: a judgment input is present only
  while the judgment holds and its subject is its role's current member.
  Without it, `digest` runs on a report the verifier never judged, because
  the apply job's basis holds handed versions that do not move.
- Instruction inputs are absolute paths; criteria are library paths, which
  the run resolves under the library recorded at start.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

import pytest
import yaml

from commonplace.artifactrun import (
    AttemptResult,
    CodeJob,
    Handout,
    RunStatus,
    Stop,
    advance,
    start_run,
)
from commonplace.lib.directory_layout import Finding
from commonplace.lib.note_parser import section
from commonplace.lib.validation import directory_type_rule
from tests.commonplace.artifactrun.handlers import INTERRUPT_ENV, LOG_ENV

HANDLERS = "tests.commonplace.artifactrun.handlers"
STANDARD = "commonplace.artifactrun.handlers"

COMPLETE_BRIEF = "---\ndisposition: complete\n---\n# Brief\n"
BLOCKED_BRIEF = "---\ndisposition: blocked\n---\n# Brief\n"

MEMBER = "types/toy-member.md"
REPORT = "types/toy-report.md"
CONTRACT = "types/toy-report.schema.yaml"
"""The report's schema: the criterion the scheduling tests edit as the report's contract."""

TOY_TYPE = {
    "description": "A toy artifact for artifact-run engine tests.",
    "type": "types/type-spec.md",
    "name": "toy-set",
    "schema": "./toy-set.schema.yaml",
    "layout": {
        "membership": "closed",
        "roles": {
            "brief": {"path": "brief.md", "type": MEMBER},
            "report": {"path": "report.md", "type": REPORT, "cites": ["brief"]},
            # The other report repeats the report's `claim`, so changing the
            # report's claim refuses the other report through the generic
            # identity check.
            "other": {"path": "other.md", "type": MEMBER, "cites": ["brief", "report"],
                      "identity": [{"from": "report", "fields": ["claim"]}]},
            "summary": {"path": "summary.md", "type": MEMBER, "cites": ["report", "other"]},
            "verification": {
                "path": "verification.md",
                "type": MEMBER,
                "cites": ["report", "other", "summary"],
                "verifies": ["report", "other", "summary"],
            },
            "digest": {"path": "digest.md", "type": MEMBER, "cites": ["report", "other"]},
            "overview": {"path": "overview.md", "type": MEMBER, "cites": ["brief"]},
        },
        "required": {
            "always": ["brief", "overview"],
            "when": {
                "role": "brief",
                "field": "disposition",
                "values": {"complete": ["report", "other", "summary", "verification", "digest"]},
            },
        },
    },
}

MODEL_ROLES = {"brief": "brief", "report": "report", "other": "other", "summary": "summary",
               "verification": "verification", "digest": "digest"}
MODEL_JOBS = tuple(MODEL_ROLES)

NO_BLOCKERS = "## Blockers\n\nnone\n\n## Limits\n\nnone\n"
"""A verdict that accepts every handed subject."""


def blocking(*blockers: str, limits: tuple[str, ...] = ()) -> str:
    """A verdict whose blockers are `<role>: <reason>` entries, each refusing its role."""
    listed = "".join(f"- {limit}\n" for limit in limits) or "none\n"
    return ("## Blockers\n\n" + ("".join(f"- {b}\n" for b in blockers) or "none\n")
            + "\n## Limits\n\n" + listed)


CORRECTED = "- corrected: repaired what the verifier blocked\n"
"""The answers to a refusal carrying one blocker, as a verifier's block of one role does."""

REFUSED = "REFUSE"
"""Text every toy member type's schema refuses in a body."""


def refused_pattern(pattern: str, why: str) -> dict:
    return {"not": {"pattern": pattern}, "description": why}


def member_schema(*forbidden: str) -> dict:
    """A toy member schema: the body must not match REFUSE or any forbidden text."""
    rules = [refused_pattern(REFUSED, f"body matches the refused pattern {REFUSED}")]
    rules += [refused_pattern(re.escape(text), f"body contains the forbidden text {text!r}") for text in forbidden]
    return {"type": "object", "properties": {"body": {"allOf": rules}}}


def member_type(name: str) -> str:
    return (f"---\ntype: types/type-spec.md\nname: {name}\ndescription: A {name} in the toy artifact.\n"
            f"schema: ./{name}.schema.yaml\n---\n# {name}\n")


def as_member(role: str, text: str) -> str:
    """A worker's text as a member of `role`: the role's type added to its frontmatter."""
    kind = TOY_TYPE["layout"]["roles"][role]["type"]
    if text.startswith("---\n"):
        return f"---\ntype: {kind}\n" + text.removeprefix("---\n")
    return f"---\ntype: {kind}\n---\n{text}"


def as_text(role: str, member: str) -> str:
    """The inverse of `as_member`, so a test reads back what its worker wrote."""
    kind = TOY_TYPE["layout"]["roles"][role]["type"]
    text = member.replace(f"type: {kind}\n", "", 1)
    return text.removeprefix("---\n---\n")


def version(role: str, text: str) -> str:
    """The stored version of a worker's text written as a member of `role`."""
    from commonplace.artifactrun.store import digest

    return digest(as_member(role, text).encode())


@directory_type_rule("types/toy-set.md")
def limits_carried(artifact, *, layout, run) -> list[Finding]:
    """The summary repeats each of the verification's Limits: a finding that needs both members."""
    summary, verification = artifact.members.get("summary.md"), artifact.members.get("verification.md")
    if summary is None or verification is None:
        return []
    limits = section(verification.document.body, "Limits").strip()
    entries = [] if limits in ("", "none") else [line[2:] for line in limits.splitlines() if line.startswith("- ")]
    return [Finding("summary", f"summary.md: limit not carried: {entry}")
            for entry in entries if entry not in summary.document.body]


def record_calls(monkeypatch: pytest.MonkeyPatch) -> None:
    """Log each code-job handler call to LOG_ENV; raise KeyboardInterrupt for INTERRUPT_ENV's job."""
    resolve = CodeJob.resolve_handler

    def logged(job: CodeJob):
        handler = resolve(job)

        def call(attempt):
            log = os.environ.get(LOG_ENV)
            if log:
                with open(log, "a", encoding="utf-8") as handle:
                    handle.write(job.name + "\n")
            if os.environ.get(INTERRUPT_ENV) == job.name:
                raise KeyboardInterrupt(job.name)
            return handler(attempt)

        return call

    monkeypatch.setattr(CodeJob, "resolve_handler", logged)


def custom_run(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, edit, *, compact: bool = False) -> Coordinator:
    """A toy run whose declaration `edit` changes before the run starts; it may add jobs.

    `edit` receives the jobs by name; a compact plan's entries are keyed by
    their role, job or name.
    """
    declaration, method = toy_library(tmp_path)
    data = compact_plan() if compact else plan(method)
    jobs = {job.get("name") or job.get("role") or job.get("job"): job for job in data["jobs"]}
    edit(jobs)
    data["jobs"] = list(jobs.values())
    declaration.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    log = tmp_path / "handlers.log"
    monkeypatch.setenv(LOG_ENV, str(log))
    monkeypatch.delenv(INTERRUPT_ENV, raising=False)
    record_calls(monkeypatch)
    run_dir = tmp_path / "runs" / "custom"
    start_run(run_dir, declaration, parameters={"subject": "toy"})
    coordinator = Coordinator(run_dir=run_dir, method=method, log=log)
    coordinator.advance()
    return coordinator


def _role(role: str) -> dict:
    return {"address": "role", "source": role}


def _optional(address: str, source: str) -> dict:
    return {"address": address, "source": source, "required": False}


def plan(method: Path) -> dict:
    """The toy declaration; file inputs point into `method`."""

    def file(name: str) -> dict:
        return {"address": "file", "source": str(method / name)}

    def model(name: str, role: str, inputs: dict, outputs: list[str], max_attempts: int) -> dict:
        return {
            "name": name,
            "kind": "model",
            "role": role,
            "instruction": "instruction",
            "max-attempts": max_attempts,
            "outputs": outputs,
            "inputs": {"instruction": file(f"{name}.md"), **inputs},
        }

    def code(name: str, handler: str, inputs: dict, role: str | None = None, outputs: list[str] = ()) -> dict:
        entry = {"name": name, "kind": "code", "handler": f"{HANDLERS}.{handler}",
                 "inputs": inputs, "outputs": list(outputs)}
        if role:
            entry["role"] = role
        return entry

    def check(name: str, inputs: dict) -> dict:
        """A standard check; its role and partners come from the inputs it declares."""
        return {"name": name, "kind": "code", "handler": f"{STANDARD}.check",
                "inputs": inputs, "criteria": ["toy"], "outputs": []}

    def candidate(job: str) -> dict:
        return {"address": "output", "source": f"{job}:{job}"}

    accepted_by_verification = {
        f"{role}-verified": {
            "address": "judgment",
            "source": role,
            "relation": f"verification:verifies:{role}",
            "outcome": "accepted",
        }
        for role in ("report", "other")
    }
    return {
        "type": "types/toy-set.md",
        "criteria": {"toy": {
            "member-type": MEMBER,
            "member-schema": "types/toy-member.schema.yaml",
            "report-type": REPORT,
            "set-schema": "types/toy-set.schema.yaml",
        }},
        "jobs": [
            model("brief", "brief", {}, ["brief"], max_attempts=2),
            check("check-brief", {"candidate": candidate("brief")}),
            {**model("report", "report", {"brief": _role("brief"), "refusal": _optional("refusal", "report")},
                     ["report", "answers"], max_attempts=3),
             "parameters": {"system": "{param:subject}", "validation-role": "report"}},
            check("check-report", {
                "candidate": candidate("report"),
                "brief": _role("brief"),
                "contract": {"address": "file", "source": CONTRACT},
                # The refusal input lapses once the new candidate completes, so a
                # check takes the refusal it answers from the attempt record.
                "producer-attempt": {"address": "attempt", "source": "report"},
                "answered-refusal": _optional("handed", "producer-attempt:refusal"),
                "answers": _optional("output", "report:answers"),
            }),
            model("other", "other", {"brief": _role("brief"), "refusal": _optional("refusal", "other")},
                  ["other"], max_attempts=3),
            check("check-other", {
                "candidate": candidate("other"),
                "brief": _role("brief"),
                "report": _optional("role", "report"),
            }),
            model("summary", "summary", {
                "report": _role("report"),
                "other": _role("other"),
                "refusal": _optional("refusal", "summary"),
            }, ["summary"], max_attempts=3),
            check("check-summary", {
                "candidate": candidate("summary"),
                "report": _role("report"),
                "other": _role("other"),
            }),
            model("verification", "verification", {
                "report": _role("report"),
                "other": _role("other"),
                "summary": _role("summary"),
            }, ["verification"], max_attempts=3),
            {"name": "apply-verification", "kind": "code", "handler": f"{STANDARD}.apply_verification",
             "criteria": ["toy"], "outputs": [], "inputs": {
                "candidate": {"address": "output", "source": "verification:verification"},
                # The handed report is validated at its role, under its contract.
                "contract": {"address": "file", "source": CONTRACT},
                "verifier-attempt": {"address": "attempt", "source": "verification"},
                "report-handed": {"address": "handed", "source": "verifier-attempt:report"},
                "other-handed": {"address": "handed", "source": "verifier-attempt:other"},
                "summary-handed": {"address": "handed", "source": "verifier-attempt:summary"},
            }},
            model("digest", "digest", {
                "report": _role("report"),
                "other": _role("other"),
                **accepted_by_verification,
            }, ["digest"], max_attempts=2),
            check("check-digest", {
                "candidate": candidate("digest"),
                "report": _role("report"),
                "other": _role("other"),
            }),
            code("assemble", "assemble", {
                "brief": _role("brief"),
                # Assembly waits until the artifact minus its own role is covered.
                "coverage": {"address": "coverage"},
                **{role: _optional("role", role)
                   for role in ("report", "other", "summary", "verification", "digest")},
            }, role="overview", outputs=["overview"]),
        ],
    }


@dataclass
class Coordinator:
    """Plays the agent that calls the command and runs workers."""

    run_dir: Path
    method: Path
    log: Path
    status: RunStatus | None = None
    history: list[RunStatus] = field(default_factory=list)
    open: dict[str, Handout] = field(default_factory=dict)

    # Driving

    def advance(self, *results: AttemptResult) -> RunStatus:
        for result in results:
            self.open.pop(result.attempt, None)
        self.status = advance(self.run_dir, results=tuple(results))
        self.history.append(self.status)
        self.open.update({h.attempt: h for h in self.status.handouts})
        return self.status

    def handout(self, job: str) -> Handout:
        """The one open hand-out of `job`, whichever invocation opened it."""
        matches = [h for h in self.open.values() if h.job == job]
        assert len(matches) == 1, f"expected one open hand-out of {job}, got {sorted(h.job for h in self.open.values())}"
        return matches[0]

    def write(self, handout: Handout, primary: str, **auxiliary: str) -> None:
        names = list(handout.outputs)
        # Toy jobs write toy members; another consumer's tests write their own documents.
        text = as_member(MODEL_ROLES[handout.job], primary) if handout.job in MODEL_ROLES else primary
        handout.outputs[names[0]].write_text(text, encoding="utf-8")
        handout.worker_identity.write_text('{"model": "test-model", "effort": "medium"}\n', encoding="utf-8")
        for name, text in auxiliary.items():
            handout.outputs[name].write_text(text, encoding="utf-8")

    def result(self, job: str, primary: str, **auxiliary: str) -> AttemptResult:
        """Write a worker's outputs for the open hand-out of `job`; return its result."""
        return self.result_for(self.handout(job), primary, **auxiliary)

    def result_for(self, handout: Handout, primary: str, **auxiliary: str) -> AttemptResult:
        self.write(handout, primary, **auxiliary)
        return AttemptResult(handout.attempt, model="test-model", effort="low")

    def complete(self, job: str, primary: str, **auxiliary: str) -> RunStatus:
        return self.advance(self.result(job, primary, **auxiliary))

    def fail(self, job: str, reason: str) -> RunStatus:
        handout = self.handout(job)
        return self.advance(AttemptResult(handout.attempt, outcome="failed", reason=reason))

    # Observing

    def handed(self) -> set[str]:
        """Jobs this invocation handed out."""
        return {h.job for h in self.status.handouts}

    def stopped(self) -> set[str | None]:
        return {stop.job for stop in self.status.stops}

    def stop(self, job: str) -> Stop:
        matches = [stop for stop in self.status.stops if stop.job == job]
        assert matches, f"expected a stop naming {job}, got {self.status.stops}"
        return matches[0]

    def member(self, role: str) -> str | None:
        """The member as its worker wrote it, without the type the coordinator added."""
        path = self.run_dir / "artifact" / TOY_TYPE["layout"]["roles"][role]["path"]
        return as_text(role, path.read_text(encoding="utf-8")) if path.exists() else None

    def ran(self) -> list[str]:
        """Code jobs run since the last call, in order; resets the log."""
        lines = self.log.read_text(encoding="utf-8").splitlines() if self.log.exists() else []
        self.log.write_text("", encoding="utf-8")
        return lines

    def reachable(self, handout: Handout) -> str:
        """The prompt plus every existing file it names, as one text."""
        prompt = handout.prompt.read_text(encoding="utf-8")
        texts = [prompt]
        for token in re.findall(r"[\w./@+-]+", prompt):
            for candidate in (Path(token), self.run_dir / token, handout.prompt.parent / token):
                if candidate.is_file() and candidate != handout.prompt:
                    texts.append(candidate.read_text(encoding="utf-8", errors="replace"))
                    break
        return "\n".join(texts)

    # Method edits

    def edit_method(self, name: str, text: str) -> None:
        (self.method / name).write_text(text, encoding="utf-8")

    @property
    def contract(self) -> Path:
        """The report's schema in the library, a criterion of the report's check."""
        return self.method.parents[1] / CONTRACT

    def forbid(self, text: str) -> None:
        """Change the report's contract so a report containing `text` fails validation."""
        self.contract.write_text(yaml.safe_dump(member_schema(text)), encoding="utf-8")

    def edit_contract(self) -> None:
        """Change the report's contract without changing what it accepts."""
        schema = yaml.safe_load(self.contract.read_text(encoding="utf-8"))
        schema["$comment"] = f"edit {schema.get('$comment', '')}".strip()
        self.contract.write_text(yaml.safe_dump(schema), encoding="utf-8")

    # Common stretches of a run

    def through_brief(self, brief: str = COMPLETE_BRIEF) -> RunStatus:
        assert self.handed() == {"brief"}
        return self.complete("brief", brief)

    def through_records(self, report: str = "report A\n", other: str = "other O1\n",
                        summary: str = "summary S1\n") -> RunStatus:
        """From a fresh run to the first verification hand-out."""
        self.through_brief()
        self.advance(self.result("report", report, answers=""), self.result("other", other))
        self.complete("summary", summary)
        assert "verification" in self.handed()
        return self.status

    def through_publication(self) -> RunStatus:
        """From a fresh run to a publishable artifact."""
        self.through_records()
        self.complete("verification", NO_BLOCKERS)
        self.complete("digest", "digest D1\n")
        assert self.status.publishable, self.status
        return self.status


def compact_plan() -> dict:
    """The toy plan in compact form: the writing jobs and assembly; the checks are derived.

    Instructions are relative to the plan's directory. Its expansion and the
    hand-written `plan` run the same scenarios.
    """

    def role(name: str, reads: dict, max_attempts: int, **more) -> dict:
        return {"role": name, "instruction": f"{name}.md", "max-attempts": max_attempts,
                "reads": reads, **more}

    return {
        "type": "types/toy-set.md",
        "jobs": [
            role("brief", {}, 2),
            role("report", {"brief": "required"}, 3, outputs=["report", "answers"],
                 parameters={"system": "{param:subject}"}),
            role("other", {"brief": "required"}, 3),
            role("summary", {"report": "required", "other": "required"}, 3),
            role("verification", {"report": "required", "other": "required", "summary": "required"}, 3),
            role("digest", {"report": "required", "other": "required"}, 2, **{"verified-by": ["verification"]}),
            {"name": "assemble", "kind": "code", "handler": f"{HANDLERS}.assemble", "role": "overview",
             "outputs": ["overview"], "inputs": {
                 "brief": _role("brief"),
                 "coverage": {"address": "coverage"},
                 **{name: _optional("role", name)
                    for name in ("report", "other", "summary", "verification", "digest")}}},
        ],
    }


def toy_library(tmp_path: Path, *, compact: bool = False) -> tuple[Path, Path]:
    """Write the toy type and plan under tmp_path/kb; return (declaration, method dir)."""
    kb = tmp_path / "kb"
    types = kb / "types"
    types.mkdir(parents=True)
    (types / "toy-set.md").write_text(
        "---\n" + yaml.safe_dump(TOY_TYPE, sort_keys=False) + "---\n\n# Toy set\n", encoding="utf-8"
    )
    (types / "toy-set.schema.yaml").write_text(yaml.safe_dump({"type": "object"}), encoding="utf-8")
    for name in ("toy-member", "toy-report"):
        (types / f"{name}.md").write_text(member_type(name), encoding="utf-8")
        (types / f"{name}.schema.yaml").write_text(yaml.safe_dump(member_schema()), encoding="utf-8")
    method = kb / "instructions" / "toy"
    method.mkdir(parents=True)
    for job in MODEL_JOBS:
        (method / f"{job}.md").write_text(f"# {job}\n\nWrite the {job}.\n", encoding="utf-8")
    declaration = method / "jobs.yaml"
    data = compact_plan() if compact else plan(method)
    declaration.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return declaration, method

