"""Review notes against criteria with headless workers, keeping one result file per pair.

    commonplace-review status [NOTES... [--criteria C...]] [--outcome O...] [--fresh | --stale] [--json]
    commonplace-review run gates NOTES... (--criteria C... | --all-gates) [--grouping {pair,bundle}]
                                 [--profile NAME] [--max-workers N] [--timeout SECONDS] [--force]
                                 [--resume RUN_DIR]
    commonplace-review run full-pass NOTE [--direction TEXT] [--profile NAME] [--max-workers N]
                                     [--timeout SECONDS]
    commonplace-review run revise ARTIFACT [--purpose TEXT] [--defend CLAIM ...] [--plan FILE]
                                  [--profile-simple NAME] [--profile-judgment NAME] [--timeout SECONDS]
    commonplace-review packet NOTE_OR_PACKET       # whether a full-pass packet's hashes match the files now
    commonplace-review retry RUN JOB [--key KEY]   # dismiss a worker problem or an answer; a rerun asks again
    commonplace-review acknowledge RUN LAUNCH      # confirm a launch an earlier controller left unsettled has stopped

NOTES are files or directories (a directory means its reviewable notes, not
recursively). C are gate ids, bundle names or the lenses `type`, `collection`
and `critique`. `status` without `--criteria` covers all gates (critique stays
opt-in); `run gates` launches one worker per stale pair, so it takes all gates
only when asked with `--all-gates`. `--grouping bundle` asks one worker per
note and bundle of catalog gates for that bundle's stale gates, sharing one
launch's fixed context; type, collection and critique pairs stay one call each.

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
kb/reports/state/review/runs/<workflow>/<note path without .md>/<first 12
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
for an accepted `keep` whose closing is `ready`, writes the gate result files
once at its end for the text the note then holds, keeps the note's current
packet under kb/reports/state/review/packets/, and returns a pending packet
that still matches the note instead of starting. `--direction` hands the
packet ask the operator's direction, such as the choice an undetermined
update asks for; with it, a pending packet does not block, and the packet is
decided again over the same method reports. It prints a JSON report and
exits 0 for an accepted edit or a hand-back packet with a clean guard, and
for a returned pending packet; 1 for a stop, a conflict or a guard change;
and 2 when the command failed. `packet` exits 0 when every recorded hash
matches, 1 otherwise.

`run revise` revises one markdown artifact through the simplification
passes (see `commonplace.lib.review_workflows.revise` and the library's
instructions/simplification-passes/revise-an-article-or-note.md). The first
invocation assesses and stops, writing `artifact/assessment.md` and
`artifact/plan.yaml` in the run directory. Edit the plan in place, then
repeat the command: it runs the plan's passes in order, each on the text the
one before left. `--plan FILE` copies another plan file into the run as its
plan; a repeat without it keeps that plan, and on a new run it skips the
assessment. A pass whose list the operator strikes (plain-wording,
abstractions) stops with `artifact/<pass>-list-<key>.md`: delete the entries
you strike and repeat the command. A stop for the operator is a normal end:
the JSON report's `waiting-for` gives what to do, the file and the command to
repeat. The
artifact is written once, when every pass of the plan ended `applied`,
`no-change` or `skipped`; otherwise `not-applied` names the file that holds
the proposed text. Each pass's `effort` picks its profile from the profile
file's `effort` mapping; `--profile-simple` and `--profile-judgment`
override it. An invalid plan is a command error (exit 2); the run exits 0
when it completes or waits with a clean guard, and 1 for a stop, a conflict
or a guard change.

`run gates` opens a new run under kb/reports/state/review/runs/<UTC stamp>/,
or continues RUN_DIR with `--resume`, which replays the calls whose work is
unchanged; give the same NOTES and criteria again. It prints a JSON report and
exits 0 only when every pair has a current result and the checkout guard saw
no change, 1 otherwise, and 2 when the command failed. A pair whose result
was written is fresh, so a rerun after `retry` of its answer needs `--force`.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from dataclasses import asdict
from pathlib import Path

from commonplace.headless.harness import HARNESSES, Profile
from commonplace.headless.jobs import RunLocked, acknowledge_stopped, dismiss
from commonplace.lib.review_workflows import edits, full_pass, gates, results, revise
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
    sweep.add_argument("notes", nargs="+")
    chosen = sweep.add_mutually_exclusive_group(required=True)
    chosen.add_argument("--criteria", nargs="+")
    chosen.add_argument("--all-gates", action="store_true", help="every bundle plus `type` and `collection`")
    sweep.add_argument("--grouping", choices=gates.GROUPINGS, default="pair",
                       help="one call per pair, or per note and bundle of catalog gates (default: pair)")
    sweep.add_argument("--profile", help=f"worker profile from the library's {gates.PROFILES_REL} "
                       "(default: its `default`)")
    sweep.add_argument("--max-workers", type=int, default=4, help="workers running at once")
    sweep.add_argument("--timeout", type=float, help="seconds a launch may take")
    sweep.add_argument("--force", action="store_true", help="review fresh pairs too")
    sweep.add_argument("--resume", type=Path, help="continue this run directory instead of opening a new one")
    full = workflows.add_parser("full-pass", help="run the full improvement pass over one note")
    full.add_argument("note")
    full.add_argument("--direction", help="the operator's direction for the packet, which prevails; "
                      "recorded with the run, and a pending packet does not block it")
    full.add_argument("--profile", help=f"worker profile from the library's {gates.PROFILES_REL}")
    full.add_argument("--max-workers", type=int, default=4, help="workers running at once")
    full.add_argument("--timeout", type=float, help="seconds a launch may take")
    rev = workflows.add_parser("revise", help="revise one markdown artifact through the simplification passes")
    rev.add_argument("artifact")
    rev.add_argument("--purpose", help="who the reader is and what they should notice or be able to do")
    rev.add_argument("--defend", action="append", default=[], metavar="CLAIM",
                     help="a claim the passes may not narrow; repeat for each")
    rev.add_argument("--plan", type=Path, help="the plan to run (default: the run's artifact/plan.yaml)")
    for effort in revise.EFFORTS:
        rev.add_argument(f"--profile-{effort}", help=f"profile for {effort} passes (default: the profile file's "
                         f"`effort` mapping)")
    rev.add_argument("--timeout", type=float, help="seconds a launch may take")
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
    return parser


def _root() -> Path:
    return Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], check=True, capture_output=True,
                               text=True).stdout.strip())


def _pairs(root: Path, arguments: argparse.Namespace) -> list[gates.Pair]:
    return gates.pairs(root, gates.note_paths(root, arguments.notes), arguments.criteria)


def _keep(row: results.Row, arguments: argparse.Namespace) -> bool:
    fresh = row.freshness.state == "fresh"
    return ((not arguments.outcome or row.outcome in arguments.outcome)
            and not (arguments.fresh and not fresh) and not (arguments.stale and fresh))


def _status(root: Path, arguments: argparse.Namespace) -> int:
    if arguments.notes:
        rows = results.status(root, [(pair.note, pair.criterion) for pair in _pairs(root, arguments)])
        orphans = results.orphaned(root)
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
    (run_dir / SWEEP).write_text(json.dumps({"profile": asdict(profile)}, indent=2), encoding="utf-8")
    return profile


def _options(run_dir: Path, given: dict) -> dict:
    """The options this run recorded, with each option given now (not None) in place of its value; recorded again."""
    path = run_dir / SWEEP
    options = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    options |= {key: value for key, value in given.items() if value is not None}
    run_dir.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(options, indent=2), encoding="utf-8")
    return options


def _gates(root: Path, arguments: argparse.Namespace, harnesses) -> int:
    wanted = _pairs(root, arguments)
    run_dir = _run_dir(root, arguments.resume)
    profile = _profile(root, run_dir, arguments.profile, arguments.resume is not None)
    report = gates.sweep(root, wanted, profile, run_dir, max_workers=arguments.max_workers,
                         timeout=arguments.timeout, force=arguments.force, grouping=arguments.grouping,
                         harnesses=harnesses)
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.ok else 1


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
    names = {effort: getattr(arguments, f"profile_{effort}") for effort in revise.EFFORTS}
    recorded = json.loads((run_dir / SWEEP).read_text(encoding="utf-8")) if (run_dir / SWEEP).is_file() else {}
    profiles = recorded.get("profiles") or {effort: asdict(profile)
                                            for effort, profile in revise.effort_profiles(root, names).items()}
    profiles |= {effort: asdict(load_profile(root, name, gates.profiles())) for effort, name in names.items() if name}
    options = _options(run_dir, {"purpose": arguments.purpose, "defend": arguments.defend or None,
                                 "profiles": profiles})
    if named_plan is not None:                             # the operator's answer in the plan's slot
        kept = run_dir / "artifact" / revise.PLAN
        kept.parent.mkdir(parents=True, exist_ok=True)
        kept.write_text(named_plan, encoding="utf-8")
    report = revise.revise(root, artifact, {effort: Profile(**entry) for effort, entry in profiles.items()}, run_dir,
                           purpose=options.get("purpose"), defend=options.get("defend", []),
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


def main(argv: list[str] | None = None, *, harnesses=HARNESSES) -> int:
    """Run the command; `harnesses` lets tests substitute a fake worker."""
    arguments = _parser().parse_args(sys.argv[1:] if argv is None else argv)
    try:
        root = _root().resolve()
        if arguments.command == "status":
            return _status(root, arguments)
        if arguments.command == "run":
            if arguments.workflow == "full-pass":
                return _full_pass(root, arguments, harnesses)
            if arguments.workflow == "revise":
                return _revise(root, arguments, harnesses)
            return _gates(root, arguments, harnesses)
        if arguments.command == "packet":
            return _packet(root, arguments)
        run_dir = (root / arguments.run).resolve()
        if arguments.command == "retry":
            print(json.dumps(dismiss(run_dir, arguments.job, arguments.key), indent=2))
        else:
            acknowledge_stopped(run_dir, root, arguments.launch)
            print(f"acknowledged: {arguments.launch}")
    except RunLocked as held:
        print(f"commonplace-review: another process runs this review: {held}", file=sys.stderr)
        return 2
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"commonplace-review: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
