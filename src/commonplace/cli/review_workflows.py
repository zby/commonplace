"""Review notes against criteria with headless workers, keeping one result file per pair.

    commonplace-review status [NOTES... [--criteria C...]] [--outcome O...] [--fresh | --stale] [--json]
    commonplace-review run gates NOTES... (--criteria C... | --all-gates) [--grouping {pair,bundle}]
                                 [--profile NAME] [--max-workers N] [--timeout SECONDS] [--force]
                                 [--resume RUN_DIR]
    commonplace-review run full-pass NOTE [--direction TEXT] [--profile NAME] [--max-workers N]
                                     [--timeout SECONDS]
    commonplace-review run edit OPERATION NOTE [--input ROLE=PATH ...] [--text PATH] [--profile NAME]
                                [--timeout SECONDS]
    commonplace-review run edit --fixture PATH
    commonplace-review run revise ARTIFACT [--plan FILE | --assess] [--purpose TEXT] [--defend CLAIM ...]
                                  [--profile-simple NAME] [--profile-judgment NAME] [--timeout SECONDS]
    commonplace-review approve RUN FILE --key KEY # approve the current proposal; launches nothing
    commonplace-review packet NOTE_OR_PACKET       # whether a full-pass packet's hashes match the files now
    commonplace-review retry RUN JOB [--key KEY]   # dismiss a worker problem or an answer; a rerun asks again
    commonplace-review acknowledge RUN LAUNCH      # confirm a launch an earlier controller left unsettled has stopped
    commonplace-review decisions [--note PATH] [--class NAME] [--json]  # the operator-decision record; read-only

NOTES are files or directories (a directory means its reviewable notes, not
recursively). C are gate ids, bundle names, the lenses `type` and
`collection`, compression check ids (`compression/core-claim-obscured`,
`compression/branch-bloat`, `compression/detail-overhang`,
`compression/marginal-value-redundancy`), one id per check, and the report
instructions `critique`, `friction`, `premises` and `compression-synthesis`.
`status` without `--criteria` covers all gates (compression checks and report
instructions stay opt-in); `run gates` launches one worker per stale pair, so
it takes all gates only when asked with `--all-gates`. `--grouping bundle`
asks one worker per note and bundle of catalog gates for that bundle's stale
gates, sharing one launch's fixed context; every other pair stays one call.

`compression-synthesis` runs alone on one note and takes the findings it
synthesizes as `--input ROLE=PATH` files, such as the four compression check
results; it never runs the checks. Like every run with `--input`, it writes no
current result and is never skipped as fresh. Its freshness is unassessed, so
`status` refuses it; inspect its retained observation with `show RUN`.

`status` with NOTES shows each applicable pair, including pairs never
reviewed (`missing`); without NOTES it shows every stored result whose note
and criterion still exist. `--outcome` keeps the rows whose stored outcome is
one of those given, `--fresh` the rows with a fresh result, and `--stale` the
rows without one (stale or missing): `--fresh --outcome warn` lists the
current warnings, `--stale` what a sweep would ask. Orphaned results, whose
note or criterion is gone, are listed apart and are not filtered; removing
one is deleting its file. `--json` gives each row's result file, so a fixer
can read the finding.

`run full-pass` and `run revise` keep their run under
kb/reports/state/review/runs/v2/<workflow>/<note path without .md>/<first 12
hex of the note's SHA-256>/. Repeating the command on the same note text
continues that run: answered calls replay. An edited note has another hash,
so the same command opens a new run. A repeat reuses the options the run
recorded (full pass: `--profile` and `--direction`; revise: `--purpose`,
`--defend` and the effort profiles); an option given on a repeat replaces
the recorded value.
Each workflow writes the note at most once, at its end, and only from the
text the run started from; a note changed during the run is a conflict, and
the proposed text stays in the run directory.

`run full-pass` runs the full improvement pass over one note (see
`commonplace.lib.review_workflows.full_pass` and the library's
instructions/run-full-improvement-pass-on-note.md). It writes the note only
for an accepted `keep` whose closing is `ready` and whose final publication
manifest has explicit approval, writes the gate result files
once at its end for the text the note then holds, keeps the note's current
packet under kb/reports/state/review/packets/, and returns a pending packet
that still matches the note instead of starting. `--direction` hands the
packet ask the operator's direction, such as the choice an undetermined
update asks for; with it, a pending packet does not block, and the packet is
decided again over the same method reports. It prints a JSON report and
exits 0 for an accepted edit, a publication-approval stop or a hand-back packet
with a clean guard, and for a returned pending packet; 1 for a stop, a conflict or a guard change;
and 2 when the command failed. `packet` exits 0 when every recorded hash
matches, 1 otherwise.

`run edit` runs one edit operation (types/edit-operation.md) on one note and
writes nothing to the checkout (see `commonplace.lib.review_workflows.edit_operations`).
Its typed edit result and candidate stay in the run's observation under
artifact/edits/. `--text` edits a repository file's text in place of the
note's; `--input ROLE=PATH` supplies a file the operation reads under ROLE. A
`per-item` operation returns `proposed`; given `--input answers=PATH`, the
answered strike list, it applies the unstruck entries and returns `changed`.
It exits 0 for an accepted result other than `problem` with a clean guard,
1 otherwise, and 2 when the command failed.

`run revise` revises one markdown artifact through the simplification
passes (see `commonplace.lib.review_workflows.revise` and the library's
instructions/simplification-passes/revise-an-article-or-note.md). The first
invocation requires `--plan FILE` for fixed-plan execution or `--assess` to
choose the work through assessment. Only `--assess` uses `--purpose` and
`--defend`; a fixed plan carries those fields itself. Assessment runs the
plan's settled passes automatically, retaining `artifact/assessment.md` and
`artifact/plan.yaml` for inspection. A repeat keeps the recorded mode and plan.
`--plan FILE` also overrides a stopped plan. Editing the retained plan alone
does not change workflow inputs. Changed artifact text starts a new run and
requires the mode again; runs recorded without a mode also require an explicit
choice before continuing. `run gates NOTE --criteria GATE-ID --grouping pair`
is the report-only, single-criterion baseline; `run full-pass` includes planning.
A `per-item` pass (plain-wording, abstractions) stops with its proposals in
`artifact/<pass>-list-<key>.md`: mark each entry you strike with an indented
`struck: <reason>` line, approve, then repeat. A stop for the operator is a normal end. The JSON report's
`waiting-for` gives what to do, the file, proposal key, approval command and
command to repeat. A repeat never approves and launches nothing at an
unchanged unapproved stop. Approval captures the file's text: later edits
have no effect until approved again, and the report lists such a file under
`unapproved-edits`. A plan with `stop` set ends the run; override it by explicitly
supplying a revised plan with `--plan`. Changed selection inputs require fresh
approval, and an old approval key is refused. Only the operator, or an agent
on the operator's stated word for that proposal, may approve. The
artifact is written once, only after every pass ended `applied`, `no-change` or
`skipped` and final publication is approved. Otherwise `not-applied` explains
why the candidate remains private. Both editing workflows retain `final.md`,
`final.diff` and `publication.json` under the run's `artifact/`. Inspect the
candidate and diff, approve the unchanged publication manifest, then repeat.
The manifest binds the original, candidate and decision context; an edited
manifest cannot authorize replacement text. Candidate files are outputs, not
editable workflow inputs. A no-change result needs no publication approval. Each pass's `effort` picks its profile from the profile
file's `effort` mapping; `--profile-simple` and `--profile-judgment`
override it. An invalid plan is a command error (exit 2); the run exits 0
when it completes or waits with a clean guard, and 1 for a stop, a conflict
or a guard change.

`run gates` opens a new run under kb/reports/state/review/runs/v2/<UTC stamp>/,
or continues RUN_DIR with `--resume`, which replays the calls whose work is
unchanged; give the same NOTES and criteria again. It prints a JSON report and
exits 0 only when every pair has a current result and the checkout guard saw
no change, 1 otherwise, and 2 when the command failed. A pair whose result
was written is fresh, so a rerun after `retry` of its answer needs `--force`.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from dataclasses import asdict
from pathlib import Path

from commonplace.headless import operator
from commonplace.headless.harness import HARNESSES, Profile
from commonplace.headless.jobs import RunLocked, acknowledge_stopped, dismiss, run_lock
from commonplace.lib import frontmatter
from commonplace.lib.review_workflows import (
    criteria,
    decisions,
    edit_operations,
    edits,
    fixtures,
    full_pass,
    gates,
    observations,
    result_contract,
    results,
    revise,
)
from commonplace.lib.tasks import load_profile

SWEEP = "sweep.json"
"""The run's profile and options, recorded so a resumed or repeated run asks the same worker."""


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="commonplace-review", description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    status = commands.add_parser("status", help="show each pair's freshness and stored outcome; launches nothing")
    status.add_argument("notes", nargs="*", help="notes or directories; without them, every stored result")
    status.add_argument("--criteria", nargs="+", help="with NOTES: gate ids, bundles or lenses (default: all gates)")
    status.add_argument("--outcome", nargs="+", action="extend", choices=results.OUTCOMES,
                        help="keep rows whose stored outcome is one of these")
    freshness = status.add_mutually_exclusive_group()
    freshness.add_argument("--fresh", action="store_true", help="keep rows with a fresh result")
    freshness.add_argument("--stale", action="store_true", help="keep rows without a fresh result (stale or missing)")
    status.add_argument("--json", action="store_true")
    run = commands.add_parser("run", help="run a review workflow")
    workflows = run.add_subparsers(dest="workflow", required=True)
    sweep = workflows.add_parser("gates", help="review each pair without a fresh result")
    sweep.add_argument("notes", nargs="*")
    chosen = sweep.add_mutually_exclusive_group(required=True)
    chosen.add_argument("--criteria", nargs="+")
    chosen.add_argument("--criterion-file", help="explicit repository-local draft gate; evidence only")
    chosen.add_argument("--fixture", help="retained single-atom fixture; every non-resume invocation is a new trial")
    chosen.add_argument("--all-gates", action="store_true", help="every bundle plus `type` and `collection`")
    sweep.add_argument("--grouping", choices=gates.GROUPINGS, default="pair",
                       help="one call per pair, or per note and bundle of catalog gates (default: pair)")
    sweep.add_argument("--profile", help=f"worker profile from the library's {gates.PROFILES_REL} "
                       "(default: its `default`)")
    sweep.add_argument("--max-workers", type=int, help="workers running at once (ordinary default: 4)")
    sweep.add_argument("--timeout", type=float, help="seconds a launch may take")
    sweep.add_argument("--force", action="store_true", help="review fresh pairs too")
    sweep.add_argument("--resume", type=Path, help="continue this run directory instead of opening a new one")
    sweep.add_argument("--input", action="append", default=[], metavar="ROLE=PATH",
                       help="explicit self-contained operational text input; copied, never recursively followed")
    show = commands.add_parser("show", help="inspect retained observations, findings and attempt diagnostics")
    show.add_argument("run", type=Path)
    show.add_argument("--observation")
    show.add_argument("--json", action="store_true")
    fixture = commands.add_parser("fixture", help="prepare retained baselines without model calls")
    fixture_commands = fixture.add_subparsers(dest="fixture_command", required=True)
    create = fixture_commands.add_parser("create")
    create.add_argument("--from", dest="source_run", required=True)
    create.add_argument("--observation", required=True)
    create.add_argument("--repair", action="append", default=[], metavar="ORIGINAL=PATH",
                        help="supply missing historical dirty content; bytes must match its recorded hash")
    create.add_argument("--substitute-current-executor", action="store_true",
                        help="explicitly retain the current executable as a substitute baseline")
    full = workflows.add_parser("full-pass", help="run the full improvement pass over one note")
    full.add_argument("note")
    full.add_argument("--direction", help="the operator's direction for the packet, which prevails; "
                      "recorded with the run, and a pending packet does not block it")
    full.add_argument("--profile", help=f"worker profile from the library's {gates.PROFILES_REL}")
    full.add_argument("--max-workers", type=int, default=4, help="workers running at once")
    full.add_argument("--timeout", type=float, help="seconds a launch may take")
    edit = workflows.add_parser("edit", help="run one edit operation on one note; writes nothing to the checkout")
    edit.add_argument("operation", nargs="?", help="the operation: a repository or library path, "
                      "such as instructions/simplification-passes/plain-wording.md")
    edit.add_argument("note", nargs="?", help="the note the operation edits")
    edit.add_argument("--input", action="append", default=[], metavar="ROLE=PATH",
                      help="a file the operation reads under ROLE, such as findings or answers; repeat for each")
    edit.add_argument("--text", help="a repository file holding the start text, in place of the note's file")
    edit.add_argument("--profile", help="worker profile (default: the profile file's `effort` mapping "
                      "for the operation's effort)")
    edit.add_argument("--timeout", type=float, help="seconds a launch may take")
    edit.add_argument("--fixture", help="retained single-edit fixture; every invocation is a new trial")
    rev = workflows.add_parser("revise", help="revise one markdown artifact through the simplification passes")
    rev.add_argument("artifact")
    rev.add_argument("--purpose", help="who the reader is and what they should notice or be able to do")
    rev.add_argument("--defend", action="append", default=[], metavar="CLAIM",
                     help="a claim the passes may not narrow; repeat for each")
    mode = rev.add_mutually_exclusive_group()
    mode.add_argument("--plan", type=Path, help="execute this fixed plan without assessment; final publication needs approval")
    mode.add_argument("--assess", action="store_true", help="opt into assessment and automatic pass selection; "
                      "new runs require --plan or --assess, repeats keep the recorded mode")
    for effort in edit_operations.EFFORTS:
        rev.add_argument(f"--profile-{effort}", help=f"profile for {effort} passes (default: the profile file's "
                         f"`effort` mapping)")
    rev.add_argument("--timeout", type=float, help="seconds a launch may take")
    approve = commands.add_parser("approve", help="explicitly approve an operator proposal; launches nothing")
    approve.add_argument("run", type=Path)
    approve.add_argument("file", type=Path, help="proposal path, relative to the repository or absolute")
    approve.add_argument("--key", required=True, help="proposal key from the waiting-for report")
    packet = commands.add_parser("packet", help="check a full-pass packet's recorded hashes against the files")
    packet.add_argument("target", help="a note, or its packet under kb/reports/state/review/packets/")
    retry = commands.add_parser("retry", help="dismiss a job's worker problems, or one answer, so a rerun asks again")
    retry.add_argument("run", type=Path)
    retry.add_argument("job", help="the job name: a pair's `<note>::<criterion-id>`, or a full-pass job "
                       "such as `packet` or `initial/compression`")
    retry.add_argument("--key", help="the answer to dismiss; otherwise the worker problems")
    acknowledge = commands.add_parser(
        "acknowledge", help="record that an unsettled worker launch has stopped; check the process first")
    acknowledge.add_argument("run", type=Path)
    acknowledge.add_argument("launch")
    listed = commands.add_parser("decisions", help="list operator and agent decisions from run operator records, "
                                 "packets and fix reports; read-only, computes no statistic")
    listed.add_argument("--note", help="only this artifact path, such as kb/theory/foo.md")
    listed.add_argument("--class", dest="cls", metavar="NAME",
                        help="only this action class: a pass name, publication, packet or fix-report")
    listed.add_argument("--json", action="store_true")
    return parser


def _root() -> Path:
    return Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], check=True, capture_output=True,
                               text=True).stdout.strip())


def _pairs(root: Path, arguments: argparse.Namespace) -> list[gates.Pair]:
    notes = gates.note_paths(root, arguments.notes)
    if getattr(arguments, "criterion_file", None):
        return [gates.Pair(note, criterion.identity, criterion.kind, results.criterion_id(root, criterion.identity))
                for note, criterion in criteria.draft(root, notes, arguments.criterion_file)]
    return gates.pairs(root, notes, arguments.criteria)


def _keep(row: results.Row, arguments: argparse.Namespace) -> bool:
    fresh = row.freshness.state == "fresh"
    return ((not arguments.outcome or row.outcome in arguments.outcome)
            and not (arguments.fresh and not fresh) and not (arguments.stale and fresh))


def _status(root: Path, arguments: argparse.Namespace) -> int:
    if arguments.notes:
        wanted = _pairs(root, arguments)
        if any(pair.kind == criteria.SYNTHESIS for pair in wanted):
            raise ValueError("compression-synthesis has no current result: its freshness is unassessed; "
                             "inspect its run with `commonplace-review show RUN`")
        rows = results.status(root, [(pair.note, pair.criterion) for pair in wanted])
        orphans = []
    elif arguments.criteria:
        raise ValueError("--criteria needs NOTES")
    else:
        rows, orphans = results.stored(root)
    rows = [row for row in rows if _keep(row, arguments)]
    orphans = [path.relative_to(root).as_posix() for path in orphans]
    if arguments.json:
        print(json.dumps({"pairs": [{"note": row.note, "criterion": row.criterion,
                                     "criterion-id": results.criterion_id(root, row.criterion),
                                     "freshness": row.freshness.state, "changed": list(row.freshness.changed),
                                     "outcome": row.outcome, "model": row.model,
                                     "result": row.path.relative_to(root).as_posix() if row.path else None}
                                    for row in rows],
                          "orphaned": orphans}, indent=2))
        return 0
    for row in rows:
        state = row.freshness.state + (f" ({', '.join(row.freshness.changed)})" if row.freshness.changed else "")
        print(f"{row.note}  {results.criterion_id(root, row.criterion)}  {state}  "
              f"{row.outcome or '-'}  {row.model or '-'}")
    for orphan in orphans:
        print(f"orphaned  {orphan}")
    return 0


def _run_dir(root: Path, resume: Path | None) -> Path:
    if resume is not None:
        run_dir = (root / resume).resolve()
        if not (run_dir / SWEEP).is_file():
            raise ValueError(f"not a review run: {resume}")
        if json.loads((run_dir / SWEEP).read_text()).get("format") != observations.VERSION:
            raise ValueError("old-format run cannot resume; retain it as evidence and start a new run")
        if not run_dir.is_relative_to((root / gates.RUNS).resolve()):
            raise ValueError("resume must name a run in the active review namespace")
        return run_dir
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    for suffix in ("", *(f"-{n}" for n in range(2, 100))):
        run_dir = root / gates.RUNS / f"{stamp}{suffix}"
        try:
            run_dir.mkdir(parents=True)
        except FileExistsError:
            continue
        return run_dir
    raise ValueError(f"no free run directory for {stamp}")


def _profile(root: Path, run_dir: Path, name: str | None, resumed: bool) -> Profile:
    """The run's profile, recorded when it opens; a resumed run keeps it."""
    if resumed:
        recorded = json.loads((run_dir / SWEEP).read_text(encoding="utf-8"))
        if "profile" not in recorded:
            raise ValueError(f"the run was opened by the {recorded.get('workflow')} workflow")
        profile = Profile(**recorded["profile"])
        if name is not None and load_profile(root, name, gates.profiles()) != profile:
            raise ValueError(f"the run was opened with another profile: {profile}")
        return profile
    profile = load_profile(root, name, gates.profiles())
    (run_dir / SWEEP).write_text(json.dumps({"format": observations.VERSION, "profile": asdict(profile)}, indent=2),
                                 encoding="utf-8")
    return profile


def _options(run_dir: Path, given: dict) -> dict:
    """The options this run recorded, with each option given now (not None) in place of its value; recorded again."""
    path = run_dir / SWEEP
    options = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    if options and options.get("format") != observations.VERSION:
        raise ValueError("old-format run is historical; start a new run")
    options |= {"format": observations.VERSION, **{key: value for key, value in given.items() if value is not None}}
    run_dir.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(options, indent=2), encoding="utf-8")
    return options


def _inputs(root: Path, given: list[str]) -> dict[str, dict[str, str]]:
    """The `--input ROLE=PATH` files, each read once from the repository: role -> origin and text."""
    supplied: dict[str, dict[str, str]] = {}
    for item in given:
        role, separator, name = item.partition("=")
        if not separator or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", role) or role in supplied:
            raise ValueError("--input needs unique ROLE=PATH entries (lowercase letters, digits and hyphens)")
        path = observations.safe_path(root, name)
        supplied[role] = {"origin": path.relative_to(root).as_posix(), "text": path.read_bytes().decode("utf-8")}
    return supplied


def _trial(root: Path, fixture: str, harnesses, family: str) -> dict:
    run_dir = _run_dir(root, None)
    observations.atomic_json(run_dir / SWEEP, {"format": observations.VERSION, "workflow": "trial"})
    with run_lock(run_dir):
        return fixtures.trial(root, fixture, run_dir, harnesses=harnesses, family=family)


def _gates(root: Path, arguments: argparse.Namespace, harnesses) -> int:
    if arguments.fixture:
        if (arguments.notes or arguments.profile or arguments.grouping != "pair" or arguments.force
                or arguments.timeout is not None or arguments.max_workers is not None or arguments.input):
            raise ValueError("fixture supplies its target, profile and configuration; overrides are not supported")
        run_dir = _run_dir(root, arguments.resume)
        if not arguments.resume:
            observations.atomic_json(run_dir / SWEEP, {"format": observations.VERSION, "workflow": "trial"})
        with run_lock(run_dir):
            report = fixtures.trial(root, arguments.fixture, run_dir, harnesses=harnesses, family="reviews")
        print(json.dumps(report, indent=2))
        return 0 if not report["stopped"] and not report["changed"] and all(
            item["state"] == "reviewed" for item in report["observations"]) else 1
    if not arguments.notes:
        raise ValueError("ordinary reviews need at least one target")
    run_dir = _run_dir(root, arguments.resume)
    profile = _profile(root, run_dir, arguments.profile, arguments.resume is not None)
    selection = {"notes": arguments.notes, "criteria": arguments.criteria,
                 "criterion-file": arguments.criterion_file, "all-gates": arguments.all_gates, "inputs": arguments.input}
    options = json.loads((run_dir / SWEEP).read_text())
    supplied = {}
    if arguments.resume:
        if options.get("selection") != selection:
            raise ValueError("resume selection differs; start a new run")
        snapshot = json.loads((run_dir / "review-request.json").read_text())
        wanted = [gates.Pair(**pair) for pair in snapshot["pairs"]]
    else:
        wanted = _pairs(root, arguments)
        supplied = _inputs(root, arguments.input)
        observations.atomic_json(run_dir / SWEEP, {**options, "selection": selection})
    report = gates.sweep(root, wanted, profile, run_dir, max_workers=arguments.max_workers or 4,
                         timeout=arguments.timeout, force=arguments.force or bool(arguments.criterion_file) or bool(arguments.input),
                         grouping=arguments.grouping, harnesses=harnesses,
                         publish_results=not bool(arguments.criterion_file) and not bool(arguments.input), operational_inputs=supplied)
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.ok else 1


def _edit(root: Path, arguments: argparse.Namespace, harnesses) -> int:
    if arguments.fixture:
        if (arguments.operation or arguments.note or arguments.input or arguments.text or arguments.profile
                or arguments.timeout is not None):
            raise ValueError("fixture supplies its operation, note, inputs and profile; overrides are not supported")
        report = _trial(root, arguments.fixture, harnesses, edit_operations.FAMILY)
        print(json.dumps(report, indent=2))
        return 0 if not report["stopped"] and not report["changed"] and all(
            item["state"] == "edited" for item in report["observations"]) else 1
    if not arguments.operation or not arguments.note:
        raise ValueError("run edit needs OPERATION and NOTE, or --fixture")
    operation = edit_operations.load(root, arguments.operation)
    note = _note(root, arguments.note)
    source = observations.safe_path(root, arguments.text) if arguments.text else root / note
    text = source.read_bytes().decode("utf-8")
    roles = _inputs(root, arguments.input)
    profile = (load_profile(root, arguments.profile, gates.profiles()) if arguments.profile
               else edit_operations.effort_profiles(root, {})[operation.effort])
    run_dir = _run_dir(root, None)
    observations.atomic_json(run_dir / SWEEP, {
        "format": observations.VERSION, "workflow": "edit", "profile": asdict(profile),
        "selection": {"operation": operation.identity, "note": note, "text": arguments.text,
                      "inputs": arguments.input}})
    report = edit_operations.run(root, operation, note, text, roles, profile, run_dir, timeout=arguments.timeout,
                                 harnesses=harnesses)
    print(json.dumps(report, indent=2))
    return 0 if report["ok"] else 1


def _note(root: Path, raw: str) -> str:
    path = (root / raw).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError(f"note not found in the repository: {raw}")
    return path.relative_to(root).as_posix()


def _full_pass(root: Path, arguments: argparse.Namespace, harnesses) -> int:
    note = _note(root, arguments.note)
    blocked = None if arguments.direction else full_pass.blocking(root, note)
    if blocked is not None:                               # no run directory for a pass that does not start
        print(json.dumps(blocked.to_dict(), indent=2))
        return 0
    run_dir = edits.run_dir(root, "full-pass", note)
    named = arguments.profile is not None or not (run_dir / SWEEP).is_file()
    options = _options(run_dir, {"profile": asdict(load_profile(root, arguments.profile, gates.profiles()))
                                 if named else None, "direction": arguments.direction})
    report = full_pass.full_pass(root, note, Profile(**options["profile"]), run_dir,
                                 max_workers=arguments.max_workers, timeout=arguments.timeout,
                                 direction=options.get("direction"), harnesses=harnesses)
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.ok else 1


def _revise(root: Path, arguments: argparse.Namespace, harnesses) -> int:
    artifact = _note(root, arguments.artifact)
    if not artifact.endswith(".md"):
        raise ValueError(f"not a markdown artifact: {artifact}")
    named_plan = None
    if arguments.plan:
        named_plan = arguments.plan.read_text(encoding="utf-8")   # a missing file is an error, not an assessment
        revise.read_plan(named_plan)
    run_dir = edits.run_dir(root, "revise", artifact)
    names = {effort: getattr(arguments, f"profile_{effort}") for effort in edit_operations.EFFORTS}
    recorded = json.loads((run_dir / SWEEP).read_text(encoding="utf-8")) if (run_dir / SWEEP).is_file() else {}
    mode = "fixed-plan" if named_plan is not None else "assess" if arguments.assess else recorded.get("mode")
    if mode not in {"fixed-plan", "assess"}:
        raise ValueError("choose --plan FILE for fixed-plan execution or --assess for planning; "
                         "a new run never chooses work implicitly")
    if mode == "fixed-plan" and not isinstance(named_plan if named_plan is not None else recorded.get("plan"), str):
        raise ValueError("fixed-plan run has no captured plan; supply --plan FILE")
    if mode == "fixed-plan" and (arguments.purpose is not None or arguments.defend):
        raise ValueError("fixed-plan execution takes purpose and defend from the plan; edit the --plan input instead")
    profiles = recorded.get("profiles") or {effort: asdict(profile)
                                            for effort, profile in edit_operations.effort_profiles(root, names).items()}
    profiles |= {effort: asdict(load_profile(root, name, gates.profiles())) for effort, name in names.items() if name}
    options = _options(run_dir, {"mode": mode, "purpose": arguments.purpose, "defend": arguments.defend or None,
                                 "profiles": profiles, "plan": named_plan})
    report = revise.revise(root, artifact, {effort: Profile(**entry) for effort, entry in profiles.items()}, run_dir,
                           purpose=options.get("purpose"), defend=options.get("defend", []),
                           named_plan=options["plan"] if mode == "fixed-plan" else None,
                           timeout=arguments.timeout, harnesses=harnesses)
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.ok else 1


def _packet(root: Path, arguments: argparse.Namespace) -> int:
    path = (root / arguments.target).resolve()
    packets = (root / full_pass.PACKETS).resolve()
    if not path.is_relative_to(packets):                  # a note, which a resolution may have removed
        if not path.is_relative_to(root):
            raise ValueError(f"not in the repository: {arguments.target}")
        path = full_pass.packet_file(root, path.relative_to(root).as_posix())
    if not path.is_file():
        raise ValueError(f"no packet: {path.relative_to(root).as_posix()}")
    checked = full_pass.check_packet(root, path)
    print(json.dumps(checked, indent=2))
    return 0 if checked["matching"] else 1


def _decisions(root: Path, arguments: argparse.Namespace) -> int:
    found = [entry for entry in decisions.entries(root)
             if arguments.note in (None, entry["note"]) and arguments.cls in (None, entry["class"])]
    if arguments.json:
        print(json.dumps(found, indent=2, ensure_ascii=False))
    else:
        print(decisions.text(found), end="")
    return 0


def _show(root: Path, arguments: argparse.Namespace) -> int:
    run = _run_dir(root, arguments.run)
    records = []
    evidence_root = root
    base = run / "artifact"
    if (run / "trial.json").exists():
        evidence_root = run / "tree"
        base = evidence_root / gates.RUNS / "trial" / "artifact"
    paths = ([observations.find(base, arguments.observation) / "observation.json"] if arguments.observation
             else sorted(path for family in observations.FAMILIES for path in base.glob(f"{family}/*/observation.json")))
    for path in paths:
        data = observations.load(path.parent)
        contracts = {item["origin"]: observations.safe_path(path.parent, item["path"]).read_bytes()
                     for item in data["inputs"] if item["role"] == "contract"}
        completed = []
        edit = data["request"]["kind"] == edit_operations.KIND
        for name in data["completed-results"]:
            if edit and not name.endswith("/result.md"):
                continue                                  # a retained candidate text, not a result
            text = observations.safe_path(path.parent, name).read_bytes().decode("utf-8")
            if edit:
                edit_operations.validate_saved(evidence_root, path.parent / name, text, contracts)
            else:
                result_contract.validate_saved(evidence_root, path.parent / name, text, contracts=contracts)
            parsed = frontmatter.parse(text)
            if not parsed.ok or parsed.data.get("type") not in (result_contract.TYPE, edit_operations.RESULT_TYPE):
                raise ValueError(f"invalid retained result: {name}")
            completed.append(parsed.data)
        records.append({**data, "results": completed})
    trial = json.loads((run / "trial-result.json").read_text()) if (run / "trial-result.json").exists() else None
    print(json.dumps({"run": run.relative_to(root).as_posix(), "observations": records, "trial": trial},
                     indent=2, ensure_ascii=False))
    return 0


def main(argv: list[str] | None = None, *, harnesses=HARNESSES) -> int:
    """Run the command; `harnesses` lets tests substitute a fake worker."""
    arguments = _parser().parse_args(sys.argv[1:] if argv is None else argv)
    try:
        root = _root().resolve()
        if arguments.command == "show":
            return _show(root, arguments)
        if arguments.command == "fixture":
            repairs = {}
            for item in arguments.repair:
                name, separator, source = item.partition("=")
                if not separator or name in repairs:
                    raise ValueError("--repair needs unique ORIGINAL=PATH entries")
                repairs[name] = source
            path = fixtures.create(root, arguments.source_run, arguments.observation,
                                   substitute_executor=arguments.substitute_current_executor, repairs=repairs)
            print(json.dumps({"fixture": path.relative_to(root).as_posix()}, indent=2))
            return 0
        if arguments.command == "status":
            return _status(root, arguments)
        if arguments.command == "run":
            if arguments.workflow == "full-pass":
                return _full_pass(root, arguments, harnesses)
            if arguments.workflow == "revise":
                return _revise(root, arguments, harnesses)
            if arguments.workflow == "edit":
                return _edit(root, arguments, harnesses)
            return _gates(root, arguments, harnesses)
        if arguments.command == "packet":
            return _packet(root, arguments)
        if arguments.command == "decisions":
            return _decisions(root, arguments)
        run_dir = _run_dir(root, arguments.run)
        if arguments.command == "approve":
            path = (root / arguments.file).resolve()
            artifact = (run_dir / "artifact").resolve()
            if not path.is_relative_to(artifact):
                raise ValueError("proposal is outside the run's artifact directory")
            print(json.dumps(operator.approve(run_dir, path.relative_to(artifact).as_posix(), arguments.key),
                             indent=2))
        elif arguments.command == "retry":
            print(json.dumps(dismiss(run_dir, arguments.job, arguments.key), indent=2))
        else:
            acknowledge_stopped(run_dir, root, arguments.launch)
            print(f"acknowledged: {arguments.launch}")
    except RunLocked as held:
        print(f"commonplace-review: another process runs this review: {held}", file=sys.stderr)
        return 2
    except (ValueError, OSError, subprocess.CalledProcessError, result_contract.ControllerError) as error:
        print(f"commonplace-review: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
