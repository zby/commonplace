"""A toy set type, a job set over it, and a scripted coordinator.

The toy job set mirrors the analysis mapping in
kb/work/workflow-requirements/analysis-workflow-as-job-set.md:

| Toy job | Analysis role | Kind |
|---|---|---|
| brief, check-brief | boundary and its check; carries the disposition | model, code |
| report, check-report | an analyst report (`R`, `check-R` in the scenarios) | model, code |
| other, check-other | a second analyst; its check has the report as input | model, code |
| summary, check-summary | reconcile | model, code |
| verify, apply-verification | verify-records and its apply job (`V`) | model, code |
| digest, check-digest | profile, gated on the verification's acceptances | model, code |
| assemble | assemble, gated on coverage | code |

Nothing here runs a model. `Coordinator` writes the files a worker would
write at the hand-out paths and reports attempt results.

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
- File inputs are absolute paths; the declaration's relative-path base is
  not specified.
"""

from __future__ import annotations

import re
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

import pytest
import yaml

from commonplace.workflow import (
    AttemptResult,
    Handout,
    RunStatus,
    Stop,
    advance,
    start_run,
)
from tests.commonplace.workflow.handlers import INTERRUPT_ENV, LOG_ENV

HANDLERS = "tests.commonplace.workflow.handlers"

COMPLETE_BRIEF = "---\ndisposition: complete\n---\n# Brief\n"
BLOCKED_BRIEF = "---\ndisposition: blocked\n---\n# Brief\n"

TOY_TYPE = {
    "description": "A toy set for workflow engine tests.",
    "type": "types/type-spec.md",
    "name": "toy-set",
    "layout": {
        "membership": "closed",
        "roles": {
            "brief": {"path": "brief.md", "type": "types/text.md"},
            "report": {"path": "report.md", "type": "types/text.md", "cites": ["brief"]},
            "other": {"path": "other.md", "type": "types/text.md", "cites": ["brief", "report"]},
            "summary": {"path": "summary.md", "type": "types/text.md", "cites": ["report", "other"]},
            "verification": {
                "path": "verification.md",
                "type": "types/text.md",
                "cites": ["report", "other", "summary"],
            },
            "digest": {"path": "digest.md", "type": "types/text.md", "cites": ["report", "other"]},
            "overview": {"path": "overview.md", "type": "types/text.md", "cites": ["brief"]},
        },
        "required": {
            "always": ["brief", "overview"],
            "by": {
                "role": "brief",
                "field": "disposition",
                "values": {"complete": ["report", "other", "summary", "verification", "digest"]},
            },
        },
    },
}

MODEL_JOBS = ("brief", "report", "other", "summary", "verify", "digest")


def _member(role: str) -> dict:
    return {"address": "member", "source": role}


def _optional(address: str, source: str) -> dict:
    return {"address": address, "source": source, "required": False}


def job_set(method: Path) -> dict:
    """The toy declaration; file inputs point into `method`."""

    def file(name: str) -> dict:
        return {"address": "file", "source": str(method / name)}

    def model(name: str, role: str, inputs: dict, outputs: list[str], max_attempts: int) -> dict:
        return {
            "name": name,
            "kind": "model",
            "role": role,
            "instruction": "instruction",
            "max_attempts": max_attempts,
            "outputs": outputs,
            "inputs": {"instruction": file(f"{name}.md"), **inputs},
        }

    def code(name: str, handler: str, inputs: dict, role: str | None = None, outputs: list[str] = ()) -> dict:
        entry = {"name": name, "kind": "code", "handler": f"{HANDLERS}.{handler}",
                 "inputs": inputs, "outputs": list(outputs)}
        if role:
            entry["role"] = role
        return entry

    def candidate(job: str) -> dict:
        return {"address": "output", "source": f"{job}:{job}"}

    accepted_by_verification = {
        f"{role}-verified": {
            "address": "judgment",
            "source": role,
            "relation": f"verification:cites:{role}",
            "outcome": "accepted",
        }
        for role in ("report", "other")
    }
    return {
        "type_spec": "types/toy-set.md",
        "jobs": [
            model("brief", "brief", {}, ["brief"], max_attempts=2),
            code("check-brief", "check_brief", {"candidate": candidate("brief")}),
            {**model("report", "report", {"brief": _member("brief"), "refusal": _optional("refusal", "report")},
                     ["report", "answers"], max_attempts=3),
             "parameters": {"system": "{param:subject}", "validation-member": "{set}/report.md"}},
            code("check-report", "check_report", {
                "candidate": candidate("report"),
                "brief": _member("brief"),
                "contract": file("contract-report.md"),
                # The refusal input lapses once the new candidate completes, so a
                # check takes the refusal it answers from the attempt record.
                "report-attempt": {"address": "attempt", "source": "report"},
                "answered": _optional("handed", "report-attempt:refusal"),
                "answers": _optional("output", "report:answers"),
            }),
            model("other", "other", {"brief": _member("brief"), "refusal": _optional("refusal", "other")},
                  ["other"], max_attempts=3),
            code("check-other", "check_other", {
                "candidate": candidate("other"),
                "brief": _member("brief"),
                "report": _optional("member", "report"),
            }),
            model("summary", "summary", {
                "report": _member("report"),
                "other": _member("other"),
                "refusal": _optional("refusal", "summary"),
            }, ["summary"], max_attempts=3),
            code("check-summary", "check_summary", {
                "candidate": candidate("summary"),
                "report": _member("report"),
                "other": _member("other"),
            }),
            model("verify", "verification", {
                "report": _member("report"),
                "other": _member("other"),
                "summary": _member("summary"),
            }, ["verification"], max_attempts=3),
            code("apply-verification", "apply_verification", {
                "verdict": {"address": "output", "source": "verify:verification"},
                "verification-attempt": {"address": "attempt", "source": "verify"},
                "report-seen": {"address": "handed", "source": "verification-attempt:report"},
                "other-seen": {"address": "handed", "source": "verification-attempt:other"},
                "summary-seen": {"address": "handed", "source": "verification-attempt:summary"},
            }),
            model("digest", "digest", {
                "report": _member("report"),
                "other": _member("other"),
                **accepted_by_verification,
            }, ["digest"], max_attempts=2),
            code("check-digest", "check_digest", {
                "candidate": candidate("digest"),
                "report": _member("report"),
                "other": _member("other"),
            }),
            code("assemble", "assemble", {
                "brief": _member("brief"),
                **{role: _optional("member", role)
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
        handout.outputs[names[0]].write_text(primary, encoding="utf-8")
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
        path = self.run_dir / "set" / TOY_TYPE["layout"]["roles"][role]["path"]
        return path.read_text(encoding="utf-8") if path.exists() else None

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
        assert "verify" in self.handed()
        return self.status

    def through_publication(self) -> RunStatus:
        """From a fresh run to a publishable set."""
        self.through_records()
        self.complete("verify", "no blockers\n")
        self.complete("digest", "digest D1\n")
        assert self.status.publishable, self.status
        return self.status


def toy_library(tmp_path: Path) -> tuple[Path, Path]:
    """Write the toy type and job set under tmp_path/kb; return (declaration, method dir)."""
    kb = tmp_path / "kb"
    types = kb / "types"
    types.mkdir(parents=True)
    (types / "toy-set.md").write_text(
        "---\n" + yaml.safe_dump(TOY_TYPE, sort_keys=False) + "---\n\n# Toy set\n", encoding="utf-8"
    )
    method = kb / "instructions" / "toy"
    method.mkdir(parents=True)
    for job in MODEL_JOBS:
        (method / f"{job}.md").write_text(f"# {job}\n\nWrite the {job}.\n", encoding="utf-8")
    (method / "contract-report.md").write_text("# Report contract\n", encoding="utf-8")
    declaration = method / "jobs.yaml"
    declaration.write_text(yaml.safe_dump(job_set(method), sort_keys=False), encoding="utf-8")
    return declaration, method


@pytest.fixture
def coordinator(tmp_path: Path, tmp_library: None, monkeypatch: pytest.MonkeyPatch) -> Iterator[Coordinator]:
    declaration, method = toy_library(tmp_path)

    log = tmp_path / "handlers.log"
    monkeypatch.setenv(LOG_ENV, str(log))
    monkeypatch.delenv(INTERRUPT_ENV, raising=False)

    run_dir = tmp_path / "runs" / "toy-1"
    start_run(run_dir, declaration, parameters={"subject": "toy"})
    coordinator = Coordinator(run_dir=run_dir, method=method, log=log)
    coordinator.advance()
    yield coordinator
