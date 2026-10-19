"""The analyse-agentic-system workflow as a script over headless workers.

One process owns the run: it opens the prepared analysis, acquires the source,
asks each role's worker through `jobs.Run`, checks every candidate with the
analysis's own checks, and drives the correction cascade in the order ADR 108
states, as ordinary calls:

    opening, acquire                       code
    boundary                               worker; stop here unless complete
    runtime                                worker
    memory | epistemic | workflow          workers, in parallel, then re-checked
                                           against each other
    reconciliation                         worker
    repeat up to the verifier's attempts:
        report-check                       code: the artifact-level findings
        report-verification                worker; its verdict is applied
        corrections: runtime first, then the other refused analysts in
        parallel; every report re-checked against the corrected ones;
        then reconciliation (fresh when its inputs changed)
    memory-profile, profile-verification   workers, corrected until accepted
    synthesis, synthesis-verification      workers, corrected until accepted
    every member re-checked, then assemble, publish   code

Every worker call is cached by content, so a rerun of the script resumes from
the cache (`jobs.py`). Attempt budgets are the plan's `max-attempts`, counted
per job over the whole run as the engine counted them: a check's rejection, a
verifier's correction, a re-ask after an input changed and a timed-out or
incomplete launch each spend one; the verifier's own budget bounds the number
of verifications (ADR 108's three record verifications; the plan's budgets
give two profile corrections and one synthesis correction). The run stops on
an exhausted budget, blockers at a verifier's last attempt, a worker's
problem, a usage limit or an environment failure; nothing is published then.

What the plan file supplies is data, not scheduling: each role's
instruction, outputs, reads, attempt budget, criteria groups, declared checks
and feedback, the frozen-source role, the type and the prompt section.
Control flow lives here. The environment is pinned: the worktree must be at
its preparation commit, clean and running its own package, which the script
asserts at start and relies on for cache replay.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys
import time
from collections.abc import Callable, Iterable, Mapping
from pathlib import Path

import yaml
from corrections import produce
from headless import HARNESSES, LaunchFailed, Profile
from jobs import Answer, OutOfAttempts, Run, digest, gather

from commonplace.artifactrun.checks import (
    Candidate,
    apply_verdict,
    artifact_check,
    check_candidate,
    frozen_source,
    refusal_findings,
)
from commonplace.artifactrun.compact import type_closure
from commonplace.artifactrun.handouts import (
    ABSENT_LINE,
    layout_bindings,
    render_prompt_section,
)
from commonplace.artifactrun.store import digest as sha256_of
from commonplace.artifactrun.worktree import (
    preparation_for,
    require_committed_startup,
    run_command,
)
from commonplace.lib.agentic_analysis import run_ids
from commonplace.lib.agentic_analysis.analyses import (
    WORKER_PROFILES,
    resolve_worker_profile,
    source_slug,
)
from commonplace.lib.agentic_analysis.guards import require_prepared_method
from commonplace.lib.agentic_analysis.opening import acquire_analysis, open_analysis
from commonplace.lib.agentic_analysis.plan import PLAN
from commonplace.lib.agentic_analysis.publication import (
    Provenance,
    assemble_analysis,
    publish_analysis,
)
from commonplace.lib.agentic_analysis.worktree import STATE_ROOT
from commonplace.lib.directory_artifact import MANIFEST_NAME
from commonplace.lib.directory_layout import Layout, type_layout
from commonplace.lib.note_parser import parse_document
from commonplace.lib.reading_batches import READ_BATCH_BYTES

RUNTIME = "runtime"
PARALLEL_ANALYSTS = ("memory", "epistemic", "workflow")
"""ADR 108's correction order: the runtime correction finishes before these start, since they read it."""
ANALYSTS = (RUNTIME, *PARALLEL_ANALYSTS)
RECONCILIATION = "reconciliation"
REPORT_VERIFICATION = "report-verification"
REPORT_CHECK = "report-check"
UNATTENDED = {"claude-code": {"permission-mode": "acceptEdits"}, "codex": {"sandbox": "workspace-write"},
              "pi": {"approve": True}}
"""Per-harness flags that let a worker read, write and run commands without a prompt (phase 0)."""
COMPLETE = "complete"
PLACEHOLDER = re.compile(r"\{(param:)?([A-Za-z0-9_-]+)\}")


class Stopped(Exception):
    """The run stops here; a rerun after the operator's repair resumes from the cache."""


class Problem(Stopped):
    def __init__(self, role: str, text: str):
        super().__init__(f"{role} reported a problem: {text.strip()}")
        self.role, self.text = role, text


def frontmatter(data: bytes) -> dict:
    document, _ = parse_document(data.decode("utf-8", errors="replace"))
    return (document.frontmatter or {}) if document is not None else {}


class Method:
    """The plan file's data: roles, their instructions, reads, budgets, checks and criteria."""

    def __init__(self, library: Path) -> None:
        self.library = library
        self.plan_dir = library / Path(PLAN).parent
        data = yaml.safe_load((library / PLAN).read_text(encoding="utf-8"))
        self.type_spec: str = data["type"]
        self.layout: Layout = type_layout((library / self.type_spec).read_text(encoding="utf-8"), self.type_spec)
        self.frozen: str = data["frozen-source"]
        self.groups: dict[str, dict[str, str]] = data.get("criteria") or {}
        self.prompt_section = (self.plan_dir / data["prompt-section"]).read_text(encoding="utf-8")
        defaults = data.get("defaults") or {}
        self.default_attempts: int = defaults.get("max-attempts", 3)
        self.parameters: dict[str, str] = dict(defaults.get("parameters") or {})
        self.roles: dict[str, dict] = {entry["role"]: entry for entry in data["jobs"] if "role" in entry}
        # Every job's outputs, so a read `job:output` is named as the engine named it.
        self.job_outputs: dict[str, list[str]] = {}
        for entry in data["jobs"]:
            if "role" in entry:
                self.job_outputs[entry["role"]] = self.outputs(entry["role"])
            else:
                self.job_outputs[entry.get("name") or entry["job"]] = list(entry.get("outputs") or ["findings"])

    def outputs(self, role: str) -> list[str]:
        return list(self.roles[role].get("outputs") or [role])

    def attempts(self, role: str) -> int:
        return self.roles[role].get("max-attempts", self.default_attempts)

    def instruction(self, role: str) -> Path:
        return (self.plan_dir / self.roles[role]["instruction"]).resolve()

    def reads(self, role: str) -> dict[str, str]:
        """What the role reads, as `source: mode`; by default its identity sources and citations."""
        declared = self.layout.roles[role]
        reads = self.roles[role].get("reads")
        if reads is None:
            sources = [*(s.role for s in declared.identity), *declared.cites]
            reads = {source: "required" for source in dict.fromkeys(sources) if source != role}
        return dict(reads)

    def extensions(self, role: str) -> dict:
        """The role's declared checks and feedback, as the engine's derived job received them."""
        entry = self.roles[role]
        return {key: entry[key] for key in ("checks", "feedback") if entry.get(key)}

    def check_inputs(self, role: str) -> dict[str, str]:
        """The reads a declared check needs, by the check's own input names."""
        inputs: dict[str, str] = {}
        for check in self.roles[role].get("checks") or []:
            if isinstance(check, dict):
                for name, read in (check.get("inputs") or {}).items():
                    inputs[name] = read["source"] if isinstance(read, dict) else read
        return inputs

    def read_name(self, source: str) -> str:
        """The prompt name of a read: a role, a single-output job, `job-output` or `role-refusal`."""
        if source.startswith("refusal:"):
            return source.removeprefix("refusal:") + "-refusal"
        if ":" in source:
            job, _, output = source.partition(":")
            return job if len(self.job_outputs[job]) == 1 else f"{job}-{output}"
        return source

    def files(self, role: str) -> dict[str, str]:
        """The criteria files the role's prompt names, by their group entry names."""
        files: dict[str, str] = {}
        for group in self.roles[role].get("criteria") or []:
            files.update(self.groups[group])
        return files

    def criteria(self) -> dict[str, bytes]:
        """Every pinned criterion the run validates against: all groups plus the types' closure."""
        paths = {path for group in self.groups.values() for path in group.values()}
        types = [self.type_spec, *(r.type for r in self.layout.roles.values())]
        # A contract file is validated by its own type too.
        types += [t for t in (frontmatter((self.library / p).read_bytes()).get("type") for p in paths
                              if p.endswith(".md")) if isinstance(t, str)]
        paths |= set(type_closure(self.library, types))
        return {path: (self.library / path).read_bytes() for path in sorted(paths)}


class Analysis:
    def __init__(self, run_dir: Path, *, timeout: float | None, max_workers: int | None,
                 harnesses=HARNESSES, sleep=time.sleep) -> None:
        self.run_dir = run_dir.resolve()
        self.worktree = self.run_dir.parents[len(STATE_ROOT.parts)]
        if self.run_dir.parent != self.worktree / STATE_ROOT:
            raise ValueError(f"{run_dir} is not directly under a worktree's {STATE_ROOT}")
        self.library = self.worktree / "kb"
        self.parameters: dict[str, str] = json.loads((self.run_dir / "parameters.json").read_text())
        self.method = Method(self.library)
        self.layout = self.method.layout
        self.criteria = self.method.criteria()
        self.profiles = (self.library / WORKER_PROFILES).read_bytes()
        worker = resolve_worker_profile(self.profiles, self.parameters["worker-profile"])
        entry = yaml.safe_load(self.profiles)["profiles"][worker["profile"]]
        profile = Profile.from_yaml_entry({**entry, "flags": {**UNATTENDED.get(entry["harness"], {}),
                                                              **entry.get("flags", {})}})
        self.run = Run(self.run_dir, self.worktree, profile, timeout=timeout, harnesses=harnesses,
                       sleep=sleep, max_workers=max_workers)
        self.budget = {role: self.method.attempts(role) for role in self.method.roles}
        self.members: dict[str, bytes] = {}          # accepted members by role
        self.latest: dict[str, Answer] = {}          # the answer each member came from
        self.code: dict[str, bytes] = {}             # code jobs' outputs: opening, acquire, report-check

    # Code jobs

    def code_job(self, name: str, compute: Callable[[], bytes]) -> bytes:
        """A code job's output, kept under `code/` so a rerun reuses it."""
        path = self.run_dir / "code" / f"{name}.json"
        if path.exists():
            self.code[name] = path.read_bytes()
            return self.code[name]
        data = compute()
        path.parent.mkdir(exist_ok=True)
        tmp = path.with_suffix(".tmp")
        tmp.write_bytes(data)
        tmp.replace(path)
        self.code[name] = data
        self.run.log(event="code", job=name)
        return data

    def opening(self) -> bytes:
        def open_run() -> bytes:
            return open_analysis(self.parameters, self.profiles, self.run_dir, self.library)
        metadata = self.code_job("opening", open_run)
        # A rerun reasserts the pins opening checked: the cache is replayed only in the environment it was made in.
        require_prepared_method(self.worktree, json.loads(metadata)["inputs-commit"], preparation_for(self.worktree),
                                job="run")
        return metadata

    # Prompts

    def prompt(self, role: str, given: Mapping[str, str]) -> str:
        """The frame the analysis workers follow: the instruction, `name = value` lines, the prompt section.

        `given` are the attempt's inputs: the role's reads, `previous-*` on a
        rerun and `refusal` when correcting; each is placed with an
        `{input:<name>}` token that `Run.ask` fills.
        """
        method, layout, library = self.method, self.layout, self.library
        outputs = method.outputs(role)
        values: dict[str, str] = {"system": self.parameters["system"], "run-id": self.run_dir.name, "role": role,
                                  **layout_bindings(layout, role)}
        values |= {name: self.parameter(template) for name, template in method.parameters.items()}
        files = {"member-type": layout.roles[role].type}
        files |= {f"{source}-type": layout.roles[source].type for source in method.reads(role)
                  if source in layout.roles and source != role}
        files |= method.files(role)
        values |= {name: str(library / path) for name, path in files.items()}
        for source in method.reads(role):
            name = method.read_name(source)
            values[name] = f"{{input:{name}}}" if name in given else ABSENT_LINE
        values["refusal"] = "{input:refusal}" if "refusal" in given else ABSENT_LINE
        values |= {name: f"{{input:{name}}}" for name in given if name.startswith("previous-")}
        values["output"] = f"{{output:{outputs[0]}}}"
        if len(outputs) > 1:
            values["output-answers"] = f"{{output:{outputs[1]}}}"
        values |= {"problem": "{problem}", "artifact": str(self.run.artifact), "scratch": "{scratch}"}
        instruction = method.instruction(role)
        lines = [f"Follow {instruction} with:", *(f"{key} = {value}" for key, value in values.items()), "",
                 render_prompt_section(method.prompt_section, values)]
        sized = [(str(library / path), (library / path).read_bytes()) for path in files.values()]
        sized += [(f"{{input:{name}}}", text.encode("utf-8")) for name, text in given.items()]
        lines += ["", "## Input reading batches", "",
                  f"Read the named job instruction {instruction} before these reading batches.", "",
                  ("Load inputs in these batches to avoid truncated reads. Read each batch's files, "
                   "grouping them in one tool call only when your read tool returns every file's complete "
                   "result, and recover any truncation before continuing. Read oversized files in bounded "
                   "ranges."), ""]
        lines += [f"{number}. " + ", ".join(batch) for number, batch in enumerate(batches(sized), 1)]
        oversized = [(path, data) for path, data in sized if len(data) > READ_BATCH_BYTES]
        if oversized:
            lines += ["", "Oversized-file ranges:",
                      ("Read each range in a separate tool call. A single oversized line still needs a smaller "
                       "read if delivery is truncated.")]
            lines += [f"- {path}: lines " + "; ".join(f"{a}-{b}" for a, b in ranges(data)) for path, data in oversized]
        return "\n".join(lines) + "\n"

    def parameter(self, template: str) -> str:
        """A plan parameter's value: `{param:<name>}` is a run parameter, `{run}` the run directory."""
        return PLACEHOLDER.sub(lambda m: self.parameters[m.group(2)] if m.group(1) else str(
            {"run": self.run_dir, "run-id": self.run_dir.name, "artifact": self.run.artifact}[m.group(2)]), template)

    def inputs(self, role: str) -> dict[str, str]:
        """The role's reads that are present now, as input texts."""
        texts: dict[str, str] = {}
        for source, mode in self.method.reads(role).items():
            value = self.read_value(source)
            if value is None:
                if mode == "required":
                    raise Stopped(f"{role} needs {source}, which the run has not produced")
                continue
            texts[self.method.read_name(source)] = value
        return texts

    def read_value(self, source: str) -> str | None:
        if source.startswith("refusal:"):
            # The engine handed a refusal of the role's latest output; a verifier runs only once
            # that output is accepted, when no such refusal exists.
            return None
        if ":" in source:
            job, _, output = source.partition(":")
            if job in self.code:
                return self.code[job].decode("utf-8")
            answer = self.latest.get(job)
            return None if answer is None else answer.outputs.get(output)
        member = self.members.get(source)
        return None if member is None else member.decode("utf-8")

    # Candidates and checks

    def candidate(self, role: str, data: bytes, exclude: Iterable[str] = ()) -> Candidate:
        """The candidate at its role beside its partners, as the engine's derived check or apply job built it.

        A producer's partners are its identity sources, its citations and
        the frozen source, with the accepted member as incumbent; a
        verifier's are the members it reads, handed as `<name>-handed`, with
        no incumbent. `exclude` leaves named roles out, so a candidate of a
        parallel round is checked against the members present before it.
        """
        method, layout = self.method, self.layout
        declared = layout.roles[role]
        verifying = bool(declared.verifies)
        if verifying:
            partners = {method.frozen, *(s for s in method.reads(role) if s in layout.roles)}
        else:
            partners = {method.frozen, *(s.role for s in declared.identity), *declared.cites}
        partners -= {role, *exclude}
        members = dict(self.members)
        snapshot = {layout.path(r): members[r] for r in partners if r in members}
        inputs = {name: self.read_value(source) for name, source in method.check_inputs(role).items()}
        if verifying:
            inputs |= {f"{method.read_name(s)}-handed": self.read_value(s) for s in method.reads(role)}
        return Candidate(
            role, data, snapshot, self.worktree, frozen_source(method.frozen, role, snapshot, layout, job=role),
            None if verifying else members.get(role), run_dir=self.run_dir, layout=layout, relations=(),
            type_spec=method.type_spec, criteria=self.criteria,
            run_values={**self.parameters, "run-id": self.run_dir.name}, frozen_source=method.frozen,
            extensions=method.extensions(role),
            inputs={name: None if value is None else value.encode("utf-8") for name, value in inputs.items()})

    def findings(self, role: str, data: bytes, exclude: Iterable[str] = ()) -> list[str]:
        """The role's own check of `data`: content and declared checks, or a verdict's own findings."""
        candidate = self.candidate(role, data, exclude)
        if self.layout.roles[role].verifies:
            return apply_verdict(candidate)[0]
        return check_candidate(candidate)

    def content_check(self, role: str, exclude: Iterable[str] = ()) -> Callable[[Answer], list[str]]:
        primary = self.method.outputs(role)[0]
        return lambda answer: self.findings(role, answer.outputs[primary].encode("utf-8"), exclude)

    def verdict_check(self, role: str, judgments: list) -> Callable[[Answer], list[str]]:
        """Reject a verdict for its own findings; otherwise keep the subject judgments it makes."""
        primary = self.method.outputs(role)[0]

        def check(answer: Answer) -> list[str]:
            own, judged = apply_verdict(self.candidate(role, answer.outputs[primary].encode("utf-8")))
            judgments[:] = judged
            return own
        return check

    # Workers

    def role_job(self, role: str, check: Callable[[Answer], list[str]], refusal: str | None = None) -> bytes:
        """Ask the role's worker, correcting `refusal` over the current member when given; accept the result.

        Without a refusal, a member whose reads are unchanged since it was
        produced is current: nothing is asked and no attempt is spent, as the
        engine ran a job only when an input changed.
        """
        outputs = self.method.outputs(role)
        inputs = self.inputs(role)
        latest = self.latest.get(role)
        if refusal is None and latest is not None and self.unchanged(latest, inputs):
            self.run.log(event="current", role=role)
            return self.members[role]
        previous = dict(latest.outputs) if latest is not None else None
        self.run.log(event="job", role=role, correcting=refusal is not None, attempts_left=self.budget[role])
        answer = produce(self.run, role, lambda given: self.prompt(role, given), check, outputs, member=role,
                         attempts=self.budget[role], refusal=refusal, previous=previous, inputs=inputs)
        self.budget[role] -= answer.attempts
        if answer.problem is not None:
            raise Problem(role, answer.problem)
        data = answer.outputs[outputs[0]].encode("utf-8")
        self.members[role], self.latest[role] = data, answer
        self.run.accept(self.layout.path(role), answer.outputs[outputs[0]])
        return data

    @staticmethod
    def unchanged(latest: Answer, inputs: Mapping[str, str]) -> bool:
        """Whether the role's reads are the ones its latest answer was asked with."""
        asked = {name: value for name, value in latest.record["inputs"].items()
                 if name != "refusal" and not name.startswith("previous-")}
        return asked == {name: digest(text) for name, text in inputs.items()}

    def recheck(self, roles: Iterable[str]) -> None:
        """Re-check accepted members against their current partners; correct any that no longer pass.

        The engine re-ran a role's check whenever a cited partner changed
        and refused the member when it failed; here the same refusal is a
        structural one the producer answers, until every member passes.
        """
        roles = list(roles)
        while True:
            failing = [(role, findings) for role in roles if (findings := self.findings(role, self.members[role]))]
            if not failing:
                return
            for role, findings in failing:
                self.run.log(event="recheck", role=role, findings=findings)
                self.role_job(role, self.content_check(role), refusal_findings(findings, member=role, answered=None))

    def apply(self, verifier: str) -> dict[str, str]:
        """Run a verifier until its verdict is well formed; return the refused subjects' refusals."""
        judgments: list = []
        self.role_job(verifier, self.verdict_check(verifier, judgments))
        verified = self.layout.roles[verifier].verifies
        refused = {j.role: j.findings for j in judgments if j.outcome == "refused"}
        accepted = {j.role for j in judgments if j.outcome == "accepted"}
        if not refused and not set(verified) <= accepted:
            raise Stopped(f"{verifier}'s blockers address none of {', '.join(verified)}")
        self.run.log(event="verdict", role=verifier, refused=sorted(refused), accepted=sorted(accepted))
        return refused

    # The workflow

    def analyse(self) -> bytes:
        metadata = self.opening()
        source = self.code_job("acquire", lambda: acquire_analysis(metadata, self.run_dir))
        boundary = self.role_job(self.method.frozen, self.content_check(self.method.frozen))
        disposition = frontmatter(boundary).get("result-disposition")
        self.run.log(event="boundary", disposition=disposition)
        if disposition == COMPLETE:
            self.reports()
            self.verified("memory-profile", "profile-verification")
            self.verified("synthesis", "synthesis-verification")
        self.assert_checked()
        return self.publish(metadata, source)

    def reports(self) -> None:
        self.role_job(RUNTIME, self.content_check(RUNTIME))
        # Each parallel candidate is checked against the members present before the round, so the
        # check does not depend on which sibling finished first; then all are re-checked together.
        gather(*(lambda r=r: self.role_job(r, self.content_check(r, exclude=PARALLEL_ANALYSTS))
                 for r in PARALLEL_ANALYSTS))
        self.recheck(PARALLEL_ANALYSTS)
        self.role_job(RECONCILIATION, self.content_check(RECONCILIATION))
        verified = self.layout.roles[REPORT_VERIFICATION].verifies
        while True:                                   # bounded by the verifier's attempts
            snapshot = {self.layout.path(r): self.members[r] for r in (self.method.frozen, *verified)}
            findings = artifact_check(snapshot, run_dir=self.run_dir, repo=self.worktree,
                                      source=frozen_source(self.method.frozen, "", snapshot, self.layout,
                                                           job=REPORT_CHECK),
                                      type_spec=self.method.type_spec, criteria=self.criteria)
            self.code[REPORT_CHECK] = findings
            refused = self.apply(REPORT_VERIFICATION)
            if not refused:
                return
            self.last_verification(REPORT_VERIFICATION)
            if RUNTIME in refused:
                self.role_job(RUNTIME, self.content_check(RUNTIME), refused[RUNTIME])
            gather(*(lambda r=r, refusal=refused[r]: self.role_job(r, self.content_check(r), refusal)
                     for r in PARALLEL_ANALYSTS if r in refused))
            self.recheck(ANALYSTS)
            # Reconciliation answers its refusal, is asked afresh when a report changed, or stays current.
            self.role_job(RECONCILIATION, self.content_check(RECONCILIATION), refused.get(RECONCILIATION))

    def verified(self, role: str, verifier: str) -> None:
        refusal = None
        while True:                                   # bounded by both roles' attempts
            self.role_job(role, self.content_check(role), refusal)
            refused = self.apply(verifier)
            if not refused:
                return
            self.last_verification(verifier)
            refusal = refused[role]

    def last_verification(self, verifier: str) -> None:
        """Blockers at the verifier's last attempt stop the run before any correction is asked (ADR 108)."""
        if self.budget[verifier] <= 0:
            raise Stopped(f"blockers at {verifier}'s last attempt")

    def assert_checked(self) -> None:
        """Every member's current bytes pass its check against the current members; a failure is a defect here."""
        failing = {role: findings for role, data in self.members.items() if (findings := self.findings(role, data))}
        if failing:
            raise Stopped("members no longer pass their checks: " + json.dumps(failing))

    def provenance(self) -> dict[str, Provenance]:
        return {role: Provenance(self.latest[role].record["model"], sha256_of(data))
                for role, data in self.members.items()}

    def publish(self, metadata: bytes, source: bytes) -> bytes:
        common = {"metadata": metadata, "source": source, "provenance": self.provenance(), "layout": self.layout,
                  "type_spec": self.method.type_spec, "criteria": self.criteria, "run_dir": self.run_dir}
        overview, manifest = assemble_analysis(dict(self.members), **common)
        self.run.accept(self.layout.path("overview"), overview.decode("utf-8"))
        self.run.accept(MANIFEST_NAME, manifest.decode("utf-8"))
        receipt = publish_analysis({**self.members, "overview": overview}, manifest=manifest, library=self.library,
                                   **common)
        (self.run_dir / "receipt.json").write_bytes(receipt)
        self.run.log(event="published", receipt=json.loads(receipt))
        return receipt


def batches(sized: list[tuple[str, bytes]]) -> list[list[str]]:
    """Reading batches over (path, bytes) pairs; as `reading_batches`, but over content known before the files exist."""
    result: list[list[str]] = []
    batch: list[str] = []
    total = 0
    for path, data in sized:
        size = len(data)
        if batch and total + size > READ_BATCH_BYTES:
            result.append(batch)
            batch, total = [], 0
        if size > READ_BATCH_BYTES:
            result.append([f"{path} — read in bounded ranges"])
        else:
            batch.append(path)
            total += size
    return result + ([batch] if batch else [])


def ranges(data: bytes) -> list[tuple[int, int]]:
    """Line ranges fitting the read budget, as `reading_ranges` computes them for a file."""
    result = []
    start, size, end = 1, 0, 0
    for end, line in enumerate(data.splitlines(keepends=True), 1):
        if size and size + len(line) > READ_BATCH_BYTES:
            result.append((start, end - 1))
            start, size = end, 0
        size += len(line)
    if end:
        result.append((start, end))
    return result


def start(worktree: Path, *, system: str, source_identity: str, source: str, source_revision: str | None,
          worker_profile: str) -> Path:
    """Allocate a run directory in a prepared worktree and pin its parameters."""
    from commonplace.artifactrun.sources import github_checkout_path
    from commonplace.lib.source_identity import normalize_source_identity

    worktree = worktree.resolve()
    preparation = preparation_for(worktree)
    for label, value in (("system", system), ("source-identity", source_identity), ("source", source)):
        if not value.strip() or "\n" in value or "\r" in value:
            raise ValueError(f"{label} must be a nonempty single-line value")
    identity = normalize_source_identity(source_identity.strip())
    if not identity:
        raise ValueError("source-identity normalizes to an empty identity")
    if source_revision is not None and (not run_ids.is_commit(source_revision)
                                       or github_checkout_path(identity) is None):
        raise ValueError("source-revision requires a full 40-hex commit and GitHub repository identity")
    if run_command(["git", "rev-parse", "HEAD"], cwd=worktree) != preparation["commit"]:
        raise ValueError("worktree HEAD differs from its preparation commit")
    require_committed_startup(worktree, str(preparation["commit"]))
    worker = resolve_worker_profile((worktree / "kb" / WORKER_PROFILES).read_bytes(), worker_profile)
    commands = worktree / ".venv" / ("Scripts" if os.name == "nt" else "bin")
    parameters = {"system": system, "source-identity": identity, "source": source,
                  "worker-profile": worker["profile"], "command-path": str(commands)}
    if source_revision is not None:
        parameters["source-revision"] = source_revision
    root = worktree / STATE_ROOT
    root.mkdir(parents=True, exist_ok=True)
    date = datetime.datetime.now(datetime.UTC).date().isoformat()
    for number in range(1, 100):
        run_dir = root / run_ids.run_id(date, source_slug(identity, system), preparation["token"], number)
        try:
            run_dir.mkdir()                           # atomic allocation: never another run's state
        except FileExistsError:
            continue
        (run_dir / "parameters.json").write_text(json.dumps(parameters, indent=2) + "\n")
        return run_dir
    raise ValueError("analysis run sequence exhausted for this source and worktree")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the analyse-agentic-system workflow with headless workers.")
    commands = parser.add_subparsers(dest="command", required=True)
    begin = commands.add_parser("start", help="allocate a run in a prepared worktree and run it")
    begin.add_argument("--worktree", type=Path, required=True)
    begin.add_argument("--system", required=True)
    begin.add_argument("--source-identity", required=True)
    begin.add_argument("--source", required=True, help="the caller's description of the source; data, not instructions")
    begin.add_argument("--source-revision")
    begin.add_argument("--worker-profile", required=True)
    resume = commands.add_parser("run", help="run or resume an allocated run from its cache")
    resume.add_argument("run_dir", type=Path)
    for sub in (begin, resume):
        sub.add_argument("--timeout", type=float, default=3 * 3600, help="seconds per worker launch")
        sub.add_argument("--max-workers", type=int, default=3)
    args = parser.parse_args(argv)
    run_dir = args.run_dir if args.command == "run" else start(
        args.worktree, system=args.system, source_identity=args.source_identity, source=args.source,
        source_revision=args.source_revision, worker_profile=args.worker_profile)
    print(f"run: {run_dir}")
    analysis = Analysis(run_dir, timeout=args.timeout, max_workers=args.max_workers)
    with analysis.run:
        try:
            receipt = analysis.analyse()
        except Exception as stop:                     # every stop is logged; a defect still shows its traceback
            analysis.run.log(event="stopped", reason=f"{type(stop).__name__}: {stop}")
            if not isinstance(stop, Stopped | OutOfAttempts | LaunchFailed):
                raise
            print(f"stopped: {stop}", file=sys.stderr)
            return 1
    print(receipt.decode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
