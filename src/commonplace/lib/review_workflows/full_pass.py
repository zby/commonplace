"""The full improvement pass over one note, as a workflow over headless workers.

The judgment lives in the library's instruction files, each handed to its
worker as the `criterion` input: the pass instruction
(`instructions/run-full-improvement-pass-on-note.md`) for the packet, the
editor and the closing status, its `## Copyedit` section alone for the
copyeditor, and each method's own instruction for the methods. Prompts here
say only how to read inputs and write outputs. Code owns the order, the
branches, the bounds it can check and every write to the checkout.

The run:

1. Captures the note's text once, as `artifact/start.md`. Every ask is
   given that text, not the file, so a rerun asks the same requests and
   replays them.
2. Asks the methods in parallel: the compression bundle, composition
   friction, premise decomposition and connect, one ask each with a
   `report` output; and every applicable catalog gate plus critique through
   the gate sweep (`gates.review`, bundle grouping), which writes ordinary
   result files and reuses a result that is fresh for this exact text.
3. Asks for the packet with `decide()`: markdown whose frontmatter carries
   `disposition`, `update` and `merge-target`, and whose body holds the
   packet sections a reader of a hand-back needs.
4. A disposition other than `keep`, or an `update` that is not
   `determined`, ends the run: the note is untouched and the packet is the
   hand-back. Otherwise an editor applies the packet's body edits and a
   copyeditor copyedits the result, each as an output that code checks
   (`bounds()`); code then writes the accepted text to the note.
5. The closing cycle asks the same methods over the written text, then the
   closing status with `decide()`: `ready` ends the run; `repair-needed`
   (once per pass) asks the editor for those defects only, writes the
   result and runs the closing cycle again; `hand-back`, or a second
   `repair-needed`, restores the start text.

Restart: a rerun with the same run directory replays every answered call.
The reports of each finished method cycle are kept in
`artifact/reports/`, keyed by cycle and text, and reused as they are,
because the gate sweep reads result files that later cycles overwrite.

Write safety: code changes the note only from the text it expects to find,
and records each change in `artifact/writes.json` as the hashes of the text
it replaced and the text it wrote, in order. A rerun replays the workflow's
decisions, and each write step that the record already holds is skipped, so
an edit is never applied twice. A step not yet recorded writes only when the
note on disk is the text it expects; any other text is a concurrent change,
and the run stops without writing. The text the pass last left in the note
is the last recorded `to`, or the start text before any write. A resumed run
opens only on that text, so it never reports on a note the operator changed
between invocations. A hand-back restores the start text under the same
rule, so it never restores over an operator's change.

What outlives the run is the packet: `artifact/packet.md`, and the note's
current packet at `kb/reports/state/review/packets/<note-path>`. Its
frontmatter records the note, the start and final text hashes, the decision,
the closing status and the resolution fields that
`instructions/resolve-full-pass-disposition.md` fills. A pass on a note
whose current packet is `pending` and still matches the note's text does not
start; it returns that packet.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

import yaml

from commonplace.headless.decisions import decide
from commonplace.headless.harness import HARNESSES, Profile
from commonplace.headless.jobs import (
    PROBLEM_REF,
    LaunchFailed,
    OutOfAttempts,
    Run,
    gather,
    input_ref,
    output_ref,
)
from commonplace.lib import frontmatter
from commonplace.lib.hashing import content_sha256_for_text as sha256
from commonplace.lib.library import library_root
from commonplace.lib.review_workflows import gates, results
from commonplace.lib.review_workflows.criteria import CRITIQUE, gates_dir
from commonplace.lib.review_workflows.edits import (
    NO_WRITES,
    Conflict,
    Stop,
    Writes,
    bounds,
    guarded_changes,
    rejection,
    validation_fails,
    write_text,
)

PACKETS = gates.STATE / "packets"
PACKET_TYPE = "types/full-pass-report.md"
INSTRUCTION_REL = "instructions/run-full-improvement-pass-on-note.md"
METHODS = {
    "compression": ("instructions/run-compression-bundle-on-note.md", "instructions/compression-bundle"),
    "friction": ("instructions/composition-friction-gate.md", None),
    "premises": ("instructions/premise-decomposition-gate.md", None),
    "connect": ("instructions/cp-skill-connect/SKILL.md", None),
}
"""Each method's instruction, and a directory of the supporting files its links name."""
ATTEMPTS = 3
DISPOSITIONS = ("keep", "revise", "delete", "merge", "rehome")
PACKET_SCHEMA = {"disposition": DISPOSITIONS, "update": ("determined", "undetermined", "none"),
                 "merge-target": (str, type(None))}
CLOSING_SCHEMA = {"status": ("ready", "repair-needed", "hand-back"),
                  "update": ("strengthened", "preserved", "weakened", "changed", "undetermined"),
                  "defects": list}
PACKET_SECTIONS = ("## Warranted contribution", "## Disposition", "## Routed attention")
"""Sections a packet never omits."""


@dataclass
class PassReport:
    run_dir: str
    note: str
    disposition: str | None = None
    update: str | None = None
    closing_status: str | None = None
    repaired: bool = False
    written: list[str] = field(default_factory=list)     # SHA-256 of each text the pass wrote, in order
    restored: bool = False
    packet: str | None = None
    blocked: bool = False             # a pending packet that still matches the note was returned
    stopped: str | None = None
    conflict: str | None = None
    changed: list[str] = field(default_factory=list)     # checkout paths the guard saw change

    @property
    def ok(self) -> bool:
        """An accepted edit or a hand-back packet, and no unexpected change in the checkout."""
        return self.stopped is None and self.conflict is None and not self.changed and self.packet is not None

    def to_dict(self) -> dict:
        data = {key.replace("_", "-"): value for key, value in asdict(self).items() if key != "changed"}
        return {"ok": self.ok, **data, "guard": {"clean": not self.changed, "changed": self.changed}}


# --- Prompts: mechanical only ---------------------------------------------------------

METHOD_PROMPT = """\
Apply one method to one note. Nobody will answer questions. If you cannot \
apply it, write {problem} instead of guessing.

The note is `{note}` in this repository; its text is {note_input}. Judge this \
input text; the file on disk may differ. The method is `{method}`; its text is \
{criterion_input}.{support}

Do the method's work yourself in this session, as its fresh, single-use \
reviewer: where it tells you to dispatch or delegate, do that work instead; \
where it names a path for its report, write the report to {report} instead; \
where it would ask the user, record the question in the report.

Output:
- Write the method's complete report to {report}. {no_writes}
"""

PACKET_PROMPT = """\
Write the packet of a full improvement pass over one note. Nobody will answer \
questions. If you cannot, write {problem} instead of guessing.

The note is `{note}` in this repository; its text at the start of the pass is \
{note_input}. The pass's instruction is {criterion_input}: write the packet as \
it directs, from these method reports over that text:
{reports}{direction}
Output:
- Write the packet to {packet}: YAML frontmatter holding exactly the decision \
fields below, then the packet's body sections from `## Warranted contribution` \
on, without an H1. Name files as repository paths in code spans; write no \
markdown links, since the packet is stored away from the note. {no_writes}
"""

EDIT_PROMPT = """\
Edit one note as a full improvement pass directs. Nobody will answer \
questions. If you cannot do it within the instruction's bounds, write \
{problem} instead of guessing.

The note is `{note}` in this repository; its current text is {note_input}. The \
pass's instruction is {criterion_input}. {task}

Output:
- Write the complete edited note, frontmatter included, to {output}. Do not \
edit the note's file: code checks your text and writes it. {no_writes}
"""

APPLY_TASK = "Apply the body edits of the packet, {packet_input}, as the instruction directs for `keep`."
REPAIR_TASK = ("Apply only the corrections of the closing defects listed in {defects_input}, as the "
               "instruction directs for `repair-needed`; the packet is {packet_input}.")

COPYEDIT_PROMPT = """\
Copyedit one note. Nobody will answer questions. If you cannot, write \
{problem} instead of guessing.

The note's text is {note_input}. The task is {task_input}. Read no other file.

Output:
- Write the complete copyedited note, frontmatter included, to {output}. {no_writes}
"""

CLOSING_PROMPT = """\
Decide the closing status of a full improvement pass over one note. Nobody \
will answer questions. If you cannot, write {problem} instead of guessing.

The note is `{note}` in this repository. Its text at the start of the pass is \
{start_input}; the text the pass left, which the reports below assessed, is \
{note_input}. The pass's packet is {packet_input} and its instruction is \
{criterion_input}: read the closing reports against the final text and choose \
the closing status as the instruction directs. This is the {cycle} closing cycle.
Closing reports:
{reports}
Output:
- Write the decision to {closing}: YAML frontmatter holding exactly the \
decision fields below (`defects` lists the exact local defects for \
`repair-needed` and is empty otherwise), then the closing-cycle record the \
instruction describes, without its heading. Name files as repository paths in \
code spans; write no markdown links. {no_writes}
"""

REPORT_NAMES = {"compression": "compression bundle", CRITIQUE: "critique-note",
                "friction": "composition-friction-gate", "premises": "premise-decomposition-gate",
                "gates": "catalog review gates, one section per gate result", "connect": "connect"}


def _report_lines(names) -> str:
    return "".join(f"- {REPORT_NAMES[name]}: {input_ref(name)}\n" for name in names)


# --- Reading and checking texts ---------------------------------------------------------

def _library_text(rel: str) -> str:
    return (library_root() / rel).read_text(encoding="utf-8")


def copyedit_task(instruction: str) -> str:
    """The instruction's `## Copyedit` section: all the copyeditor is told."""
    match = re.search(r"^## Copyedit\n(.*?)(?=^## |\Z)", instruction, re.MULTILINE | re.DOTALL)
    if match is None:
        raise ValueError(f"{INSTRUCTION_REL} has no `## Copyedit` section")
    return match.group(0).strip() + "\n"


def _headings(text: str, required) -> list[str]:
    body = frontmatter.strip(text)
    return [f"the body has no `{heading}` section" for heading in required
            if not re.search(rf"^{re.escape(heading)}", body, re.MULTILINE)]


# --- Packets ----------------------------------------------------------------------------

def packet_file(root: Path, note: str) -> Path:
    """Where a note's current packet lives: `kb/reports/state/review/packets/<note-path>`."""
    packets = (root / PACKETS).resolve()
    target = (packets / note).resolve()
    if not target.is_relative_to(packets) or target == packets:
        raise ValueError(f"packet for {note} is outside {PACKETS.as_posix()}")
    return target


def read_packet(path: Path) -> dict:
    parsed = frontmatter.parse(path.read_text(encoding="utf-8"))
    if not parsed.ok or parsed.data.get("type") != PACKET_TYPE:
        raise ValueError(f"not a full-pass packet: {path}")
    return parsed.data


def _hash_state(root: Path, rel: str | None, recorded: str | None) -> dict:
    path = root / rel if rel else None
    current = sha256(path.read_text(encoding="utf-8")) if path is not None and path.is_file() else None
    state = "missing" if current is None else "matching" if current == recorded else "changed"
    return {"path": rel, "recorded-sha256": recorded, "current-sha256": current, "state": state}


def check_packet(root: Path, path: Path) -> dict:
    """Whether a packet's recorded hashes match the note and the merge target now."""
    data = read_packet(path)
    checks = [_hash_state(root, data.get("note"), data.get("final-sha256"))]
    if data.get("merge-target"):
        checks.append(_hash_state(root, data["merge-target"], data.get("merge-target-sha256")))
    return {"packet": path.relative_to(root).as_posix(), "resolution": data.get("resolution"),
            "matching": all(check["state"] == "matching" for check in checks), "inputs": checks}


# --- The workflow ---------------------------------------------------------------------------

def _gate_requests() -> list[str]:
    return sorted(entry.name for entry in gates_dir().iterdir() if entry.is_dir()) + [CRITIQUE]


def _methods(run: Run, root: Path, note: str, text: str, cycle: str, profile: Profile,
             max_workers: int | None) -> dict[str, str]:
    """Every method's report over `text`, by name: the four method asks, `critique` and `gates`.

    The reports of a finished cycle are kept in the run's artifact and reused
    on a rerun: the gate sweep reads result files, which later cycles
    overwrite, so asking again would not give the same requests and inputs.
    """
    def method(name: str) -> str:
        rel, support_dir = METHODS[name]
        support = sorted(path for path in (library_root() / support_dir).glob("*.md")) if support_dir else []
        inputs = {"note": text, "criterion": _library_text(rel),
                  **{f"support-{path.stem}": path.read_text(encoding="utf-8") for path in support}}
        lines = "".join(f"\n- `{path.relative_to(library_root()).as_posix()}`: {input_ref(f'support-{path.stem}')}"
                        for path in support)
        task = METHOD_PROMPT.format(
            problem=PROBLEM_REF, note=note, note_input=input_ref("note"), method=rel,
            criterion_input=input_ref("criterion"), report=output_ref("report"), no_writes=NO_WRITES,
            support=f" The supporting files its links name are inputs:{lines}" if lines else "")
        answer = run.checked(f"{cycle}/{name}", lambda problems: task + rejection(problems),
                             lambda answer: [] if answer.outputs["report"].strip() else ["the report is empty"],
                             ["report"], attempts=ATTEMPTS, inputs=inputs)
        if answer.problem is not None:
            raise Stop(f"{cycle}/{name}: worker problem: {answer.problem}")
        return answer.outputs["report"]

    def reviews() -> dict[str, str]:
        wanted = gates.pairs(root, [note], _gate_requests())
        reports, stopped = gates.review(run, root, wanted, profile, grouping="bundle", texts={note: text},
                                        max_workers=max_workers)
        if stopped:
            raise Stop(stopped)
        failed = [f"{report.job}: {report.state}: {report.problem}" for report in reports
                  if report.state not in ("fresh", "reviewed")]
        if failed:
            raise Stop("; ".join(failed))
        found, sections = {}, []
        for pair in wanted:
            result = results.read_result(results.result_path(root, pair.note, pair.criterion_id))
            if pair.kind == CRITIQUE:
                found[CRITIQUE] = result.body
            else:
                sections.append(f"## {pair.criterion_id}: {result.outcome.upper()}\n\n{result.body.strip()}\n")
        found["gates"] = "\n".join(sections) or "No catalog gate applies to this note.\n"
        return found

    record = f"reports/{cycle}-{sha256(text)[:16]}.json"
    if (run.artifact / record).is_file():
        return json.loads((run.artifact / record).read_text(encoding="utf-8"))
    names = list(METHODS)
    answers = gather(*(lambda name=name: method(name) for name in names), reviews)
    found = {**dict(zip(names, answers[:-1], strict=True)), **answers[-1]}
    run.accept(record, json.dumps(found, indent=2))
    return found


def _packet_check(root: Path, note: str):
    def check(data: dict, text: str) -> list[str]:
        target, disposition = data["merge-target"], data["disposition"]
        problems = []
        if disposition == "merge":
            if not target or target == note or not (root / target).is_file():
                problems.append("`merge-target` must name an existing note other than this one for `merge`")
        elif target is not None:
            problems.append("`merge-target` must be null unless the disposition is `merge`")
        if data["update"] == "undetermined" and disposition != "keep":
            problems.append("an undetermined update is a `keep` disposition with no body edits")
        if data["update"] == "none" and disposition == "keep":
            problems.append("an update of `none` cannot keep the note")
        return problems + _headings(text, PACKET_SECTIONS)
    return check


def _edit(run: Run, job: str, root: Path, note: str, start: str, text: str, baseline: set[str], task: str,
          inputs: dict[str, str]) -> str:
    """An editor's text for `task`, checked against the pass's bounds."""
    prompt = EDIT_PROMPT.format(problem=PROBLEM_REF, note=note, note_input=input_ref("note"),
                                criterion_input=input_ref("criterion"), task=task, output=output_ref("note"),
                                no_writes=NO_WRITES)
    answer = run.checked(job, lambda problems: prompt + rejection(problems),
                         lambda answer: bounds(root, note, start, answer.outputs["note"], baseline), ["note"],
                         attempts=ATTEMPTS, inputs={"note": text, **inputs})
    if answer.problem is not None:
        raise Stop(f"{job}: worker problem: {answer.problem}")
    return answer.outputs["note"]


def _copyedit(run: Run, root: Path, note: str, start: str, edited: str, baseline: set[str],
              instruction: str) -> str:
    before = frontmatter.parse(edited).data

    def check(answer) -> list[str]:
        text = answer.outputs["note"]
        problems = bounds(root, note, start, text, baseline)
        if not problems and frontmatter.parse(text).data != before:
            problems.append("the frontmatter changed; copy it unchanged")
        return problems
    prompt = COPYEDIT_PROMPT.format(problem=PROBLEM_REF, note_input=input_ref("note"), task_input=input_ref("task"),
                                    output=output_ref("note"), no_writes=NO_WRITES)
    answer = run.checked("copyedit", lambda problems: prompt + rejection(problems), check, ["note"],
                         attempts=ATTEMPTS, inputs={"note": edited, "task": copyedit_task(instruction)})
    if answer.problem is not None:
        raise Stop(f"copyedit: worker problem: {answer.problem}")
    return answer.outputs["note"]


def _closing(run: Run, note: str, start: str, text: str, packet: str, instruction: str, cycle: str,
             reports: dict[str, str]) -> tuple[dict, str]:
    def check(data: dict, text: str) -> list[str]:
        problems = []
        if data["status"] != "hand-back" and data["update"] not in ("strengthened", "preserved"):
            problems.append(f"a {data['update']} update is a `hand-back`")
        defects = data["defects"]
        if data["status"] == "repair-needed" and not (defects and all(isinstance(d, str) and d for d in defects)):
            problems.append("`repair-needed` lists each local defect in `defects`")
        if data["status"] != "repair-needed" and defects:
            problems.append("`defects` is empty unless the status is `repair-needed`")
        return problems
    prompt = CLOSING_PROMPT.format(problem=PROBLEM_REF, note=note, start_input=input_ref("start"),
                                   note_input=input_ref("note"), packet_input=input_ref("packet"),
                                   criterion_input=input_ref("criterion"), cycle=cycle,
                                   reports=_report_lines(reports), closing=output_ref("closing"), no_writes=NO_WRITES)
    data, answer = decide(run, f"{cycle}/status", prompt, CLOSING_SCHEMA, output="closing", check=check,
                          attempts=ATTEMPTS, inputs={"start": start, "note": text, "packet": packet,
                                                     "criterion": instruction, **reports})
    if data is None:
        raise Stop(f"{cycle}/status: worker problem: {answer.problem}")
    return data, frontmatter.strip(answer.outputs["closing"]).strip()


def _packet_text(root: Path, note: str, start: str, final: str, run_id: str, decision: dict, body: str,
                 closings: list[tuple[str, str]], closing_status: str | None, repaired: bool) -> str:
    keep = decision["disposition"] == "keep" and decision["update"] == "determined"
    target = decision["merge-target"]
    data = {
        "description": f"Packet of a full improvement pass over {note}, with its disposition and resolution",
        "type": PACKET_TYPE, "note": note, "start-sha256": sha256(start), "final-sha256": sha256(final),
        "run": run_id, "disposition": decision["disposition"], "update": decision["update"],
        "merge-target": target,
        "merge-target-sha256": sha256((root / target).read_text(encoding="utf-8")) if target else None,
        "closing-status": closing_status, "repaired": repaired,
        "resolution": "not-required" if keep and closing_status == "ready" else "pending",
        "resolved-at": None, "resolution-authority": None, "resolution-summary": None,
        "resolution-rationale": None, "resulting-paths": [],
    }
    title = (results.note_parts(start) or {}).get("title") or note
    text = ("---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True) + "---\n\n"
            + f"# Full Improvement Pass: {title}\n\n" + body.strip() + "\n")
    for cycle, record in closings:
        text += f"\n## Closing cycle: {cycle}\n\n{record}\n"
    return text


def _pass(run: Run, root: Path, note: str, profile: Profile, report: PassReport, direction: str | None,
          max_workers: int | None) -> str:
    """Run the pass in `run`; return the packet text. Raises Stop."""
    start_file = run.artifact / "start.md"
    if start_file.is_file():
        start = start_file.read_text(encoding="utf-8")
    else:
        start = (root / note).read_text(encoding="utf-8")
        run.accept("start.md", start)
    instruction = _library_text(INSTRUCTION_REL)
    baseline = validation_fails(root, note, start)
    writes = Writes(run, root, note, start)
    run_id = run.root.resolve().relative_to(root.resolve()).as_posix()

    reports = _methods(run, root, note, start, "initial", profile, max_workers)
    extra = {"direction": direction} if direction else {}
    prompt = PACKET_PROMPT.format(
        problem=PROBLEM_REF, note=note, note_input=input_ref("note"), criterion_input=input_ref("criterion"),
        reports=_report_lines(reports), packet=output_ref("packet"), no_writes=NO_WRITES,
        direction=f"- the operator's direction, which prevails: {input_ref('direction')}\n" if direction else "")
    decision, answer = decide(run, "packet", prompt, PACKET_SCHEMA, output="packet",
                              check=_packet_check(root, note),
                              attempts=ATTEMPTS, inputs={"note": start, "criterion": instruction, **reports, **extra})
    if decision is None:
        raise Stop(f"packet: worker problem: {answer.problem}")
    packet = answer.outputs["packet"]
    body = frontmatter.strip(packet)
    report.disposition, report.update = decision["disposition"], decision["update"]

    def finish(final: str, closings=(), status=None) -> str:
        return _packet_text(root, note, start, final, run_id, decision, body, list(closings), status, report.repaired)

    if decision["disposition"] != "keep" or decision["update"] != "determined":
        return finish(start)

    edited = _edit(run, "edit", root, note, start, start, baseline, APPLY_TASK.format(packet_input=input_ref("packet")),
                   {"criterion": instruction, "packet": packet})
    final = _copyedit(run, root, note, start, edited, baseline, instruction)
    writes.move(start, final)
    report.written.append(sha256(final))
    closings: list[tuple[str, str]] = []
    cycle = "closing"
    while True:
        closing_reports = _methods(run, root, note, final, cycle, profile, max_workers)
        label = "initial" if cycle == "closing" else "recovery"
        status, record = _closing(run, note, start, final, packet, instruction, label, closing_reports)
        closings.append((label, record))
        if status["status"] == "ready":
            report.closing_status = "ready"
            return finish(final, closings, "ready")
        if status["status"] == "repair-needed" and not report.repaired:
            report.repaired = True
            defects = "".join(f"- {defect}\n" for defect in status["defects"])
            repaired = _edit(run, "repair", root, note, start, final, baseline,
                             REPAIR_TASK.format(defects_input=input_ref("defects"), packet_input=input_ref("packet")),
                             {"criterion": instruction, "packet": packet, "defects": defects})
            writes.move(final, repaired)
            report.written.append(sha256(repaired))
            final, cycle = repaired, "recovery"
            continue
        writes.move(final, start)                     # hand-back, or a second repair-needed
        report.restored, report.closing_status = True, "hand-back"
        return finish(start, closings, "hand-back")


def blocking(root: Path, note: str, run_id: str | None = None) -> PassReport | None:
    """The report returning the note's current packet when it is pending and still matches the note.

    A packet written by the run `run_id` does not block it, so a resumed run continues.
    """
    path = packet_file(root, note)
    if not path.is_file():
        return None
    current = read_packet(path)
    if (current.get("resolution") != "pending" or current.get("run") == run_id
            or current.get("final-sha256") != sha256((root / note).read_text(encoding="utf-8"))):
        return None
    return PassReport(current.get("run"), note, current.get("disposition"), current.get("update"),
                      current.get("closing-status"), packet=path.relative_to(root).as_posix(), blocked=True)


def full_pass(root: Path, note: str, profile: Profile, run_dir: Path, *, max_workers: int | None = None,
              timeout: float | None = None, direction: str | None = None, harnesses=HARNESSES) -> PassReport:
    """Run the full pass over the repository-relative `note` in the run at `run_dir`, new or resumed.

    `direction` is the operator's answer to an undetermined update, or any
    direction the packet must follow; it is an input of the packet ask.
    """
    root = root.resolve()
    run_id = run_dir.resolve().relative_to(root).as_posix()
    blocked = blocking(root, note, run_id)
    if blocked is not None:
        return blocked
    report = PassReport(run_id, note)
    packet_path = packet_file(root, note)
    before = gates.checkout_state(root)
    try:
        with Run(run_dir, root, profile, timeout=timeout, harnesses=harnesses, max_workers=max_workers) as run:
            text = _pass(run, root, note, profile, report, direction, max_workers)
            run.accept("packet.md", text)
            write_text(packet_path, text)
            report.packet = packet_path.relative_to(root).as_posix()
    except Conflict as conflict:
        report.conflict = str(conflict)
    except (Stop, OutOfAttempts, LaunchFailed) as stop:      # LaunchFailed includes UsageLimited
        report.stopped = str(stop)
    report.changed = guarded_changes(root, before, run_dir, note)
    return report
