"""Review notes against criteria with headless workers, keeping one result file per pair.

    commonplace-review status [NOTES... [--criteria C...]] [--outcome O...] [--fresh | --stale] [--json]
    commonplace-review run gates NOTES... (--criteria C... | --all-gates) [--grouping {pair,bundle}]
                                 [--profile NAME] [--max-workers N] [--timeout SECONDS] [--force]
                                 [--resume RUN_DIR]
    commonplace-review run edit OPERATION NOTE [--input ROLE=PATH ...] [--text PATH] [--profile NAME]
                                [--timeout SECONDS]
    commonplace-review run edit --fixture PATH
    commonplace-review run revise ARTIFACT (--plan FILE | --pass NAME | --finding RESULT | --answers FILE ...
                                            | --triage | --assess | --full)
                                  [--purpose TEXT] [--must-keep CLAIM ...]
                                  [--profile-simple NAME] [--profile-judgment NAME] [--timeout SECONDS]
    commonplace-review run rewrite NOTE --commission FILE [--profile NAME] [--timeout SECONDS]
    commonplace-review publish RUN [--revised FILE]  # publish the candidate a run held; launches nothing
    commonplace-review answers create --from QUESTION [--to PATH]  # the pending answers file; launches nothing
    commonplace-review answers record FILE       # keep answers nothing consumes as the operator's decisions
    commonplace-review record RUN                # answers files over a revise run's findings; launches nothing
    commonplace-review retry RUN JOB [--key KEY]   # dismiss a gate sweep's worker problem or answer for --resume
    commonplace-review acknowledge RUN LAUNCH      # confirm a launch an earlier controller left unsettled has stopped
    commonplace-review decisions [--note PATH] [--class NAME] [--json]  # the operator-decision record; read-only

NOTES are files or directories (a directory means its reviewable notes, not
recursively). C are gate ids, bundle names, the lenses `type` and
`collection`, compression check ids (`compression/core-claim-obscured`,
`compression/branch-bloat`, `compression/detail-overhang`,
`compression/marginal-value-redundancy`), one id per check, and the report
instructions `critique`, `friction`, `premises`, `compression-synthesis` and
`role`. `status` without `--criteria` covers all gates (compression checks and report
instructions stay opt-in); `run gates` launches one worker per stale pair, so
it takes all gates only when asked with `--all-gates`. `--grouping bundle`
asks one worker per note and bundle of catalog gates for that bundle's stale
gates, sharing one launch's fixed context; every other pair stays one call.

`compression-synthesis` runs alone on one note and takes the findings it
synthesizes as `--input ROLE=PATH` files, such as the four compression check
results; it never runs the checks. `role`, the role report, runs alone on one
note and takes the note's inbound contexts as `--input inbound=PATH`; without
`--input`, the command collects them itself (the passages under kb/ that link
to the note, outside kb/reports/ and kb/work/). Like every run with `--input`,
these write no current result and are never skipped as fresh. Their freshness
is unassessed, so `status` refuses them; inspect a retained observation with
`show RUN`.

`status` with NOTES shows each applicable pair, including pairs never
reviewed (`missing`); without NOTES it shows every stored result whose note
and criterion still exist. `--outcome` keeps the rows whose stored outcome is
one of those given, `--fresh` the rows with a fresh result, and `--stale` the
rows without one (stale or missing): `--fresh --outcome warn` lists the
current warnings, `--stale` what a sweep would ask. Orphaned results, whose
note or criterion is gone, are listed apart and are not filtered; removing
one is deleting its file. `--json` gives each row's result file, so a fixer
can read the finding.

`run revise` and `run rewrite` open a new run on every invocation, under
kb/reports/state/review/runs/v2/<workflow>/<note path without .md>/<UTC
stamp>/, with `-2`, `-3` on a collision. These names sort in time order;
runs made before this layout are named by a hash of their start text and do
not, so the time of a run is in its records, not its name. The run records the hash of the note's start text in
start.json. No run is repeated or resumed: a run that stops ends, and a later
command that acts on its output names the file or the run. The workflow
writes the note only over the run's start text; a note changed by anyone
else is a conflict, and the proposed text stays in the run directory.

`run edit` runs one edit operation (types/edit-operation.md) on one note and
writes nothing to the checkout (see `commonplace.lib.review_workflows.edit_operations`).
Its typed edit result and candidate stay in the run's observation under
artifact/edits/. `--text` edits a repository file's text in place of the
note's; `--input ROLE=PATH` supplies a file the operation reads under ROLE. A
`per-item` operation returns `proposed`. `answers create --from RESULT`
writes the pending answers file (types/answers.md) for that result; after
the operator decides its items, `--input answers=PATH` applies the
`approved` items and returns `changed`. The validator must accept the answers,
and their question must be a result of the same operation on the same text.
It exits 0 for an accepted result other than `problem` with a clean guard,
1 otherwise, and 2 when the command failed.

`run revise` revises one markdown artifact through the simplification
passes (see `commonplace.lib.review_workflows.revise` and the library's
instructions/simplification-passes/revise-an-article-or-note.md). It runs a
plan, and every invocation chooses how the plan is made: focused (a fixed
plan), quick (`--assess`) or full (`--full`). A fixed plan is `--plan FILE`,
`--pass NAME` (a one-entry plan for that pass) or `--finding RESULT` (a
one-entry plan that fixes that review result of the artifact). `--assess`,
`--full`, `--triage`, `--answers` and the one-entry plans use `--purpose` and
`--must-keep`; a plan file carries those fields itself. `--must-keep` lists
only what this run keeps beyond the note's write brief, whose Must keep every
worker already receives. The assessor also receives the artifact's fresh
stored `warn` and `fail` review results. `--full` first runs every review
operation that declares a `depth` on the artifact, as `run gates` would on
the profile file's `default` profile, in runs under the revise run
directory; then the assessor also receives the depth 1 reports, the
compression synthesis report and the role report, and may stop the plan on a
proposal to change the artifact. Assessment runs the plan's settled passes
automatically, retaining `artifact/assessment.md` and `artifact/plan.yaml`.
A plan with `stop` set ends the run with `artifact/stop-answers.md`; a
replacement plan runs with `--plan`. `run gates NOTE --criteria GATE-ID
--grouping pair` is the report-only, single-criterion baseline.

The run ends at its first stop. Before a `per-item` pass (plain-wording,
abstractions) asks for proposals, the run publishes what the earlier passes
applied; then it writes the pending answers file for the proposals as
`artifact/<pass>-answers.md` and ends. A pass that ends with a problem ends
the run after the earlier passes' work is published. The run publishes only
when the text differs from the note and adds no validation warning the note
does not have; such a candidate is held instead (below). The publication is
kept as `artifact/publications/1.md` with its diff `1.diff`, and recorded in
the run's `published.json` with its hash, the plan entries it covers and the
time; the report lists it under `publications` and says `published: true`.
Nothing is committed: `git diff` shows the change, and git reverses it.

A run that leaves work unfinished writes `continuation.json` and reports it
as `continuation`: `made-for`, the note's hash and text when the run ended,
and one item per unfinished piece of work in dependency order, each with
`kind`, `what`, `actor` (`operator`, `session-agent`, or `worker` with its
`effort`), `after` (the ids of the items to settle first), `how` (the step
of the continuation instruction and, where one exists, the `command`), the
`answers` files it waits for and its `evidence`. A plan entry not run is
continued by `run revise NOTE --plan FILE`, where FILE is a one-entry plan
the run wrote under `artifact/continue/`, with the entry's scope and the
run's purpose and must-keep list; an entry that applies the operator's
answers is continued by `--answers FILE`. A fix names the run's copy of
its review result, which no later sweep replaces. The run also keeps its
report as report.json.

`--triage` launches no review and no assessor: it writes one pending answers
file `artifact/finding-answers-<key>.md` per fresh stored `warn` or `fail`
result and ends. `--answers FILE` (repeatable) names the operator's decided
answers files; naming them is the approval, and the run keeps a copy of
each under answers/ before it launches anything. Answers over a `per-item`
pass's proposals make a run of that pass alone that applies the `approved`
items and publishes; it is refused unless the note holds exactly the text
the proposals were made for. Answers over review results, such as a
triage's, make a plan with one fix entry per result with an `approved`
finding, each receiving its answers as `finding-answers`; refused unless the
parts of the note each result's criterion watches are those it judged. Files
whose decisions nothing applies
(no item approved, a plan stop's answers, the files `record` writes) are
kept with `answers record FILE` instead.

A held candidate stays in the run as `artifact/final.md` with
`artifact/final.diff`, and the report's `held` names the warnings and the
command that publishes it. `publish RUN` publishes that exact candidate:
naming the run is the operator's approval. It is refused unless the note
still holds the text the candidate was held over (the run's start text, or
its last automatic publication), the write brief is the one the run
captured, `final.md` and `final.diff` are the ones the run held and the
operator has not published the candidate already. `--revised FILE` publishes the operator's full revised text instead,
read from a file outside the run's `artifact/`, after the candidate checks
(frontmatter, H1 and validation); the run keeps it as `artifact/revised.md`
with `artifact/revised-from-final.diff` and `artifact/revised.diff`. `publish`
launches nothing. Each pass's `effort` picks its profile from the profile
file's `effort` mapping; `--profile-simple` and `--profile-judgment`
override it. An invalid plan or refused answers are a command error (exit
2); the run exits 0 when it ends with a clean guard, completed or with work
left to continue, and 1 for a failed pass or review, a conflict or a guard
change.

`record RUN` names a revise run directory whose findings the operator
answered outside the run, such as by splitting the note. For each review
result the run's assessor or triage received that has a `warn` or `fail`
finding, it writes the pending answers file a triage writes,
`artifact/finding-answers-<key>.md`, over the run's copy of the result, and
prints each file with the command that records it. It works whether or not
the note still holds the run's text. It launches nothing, makes no plan and
publishes nothing; a file that exists, from a triage or an earlier record,
is left as it is.

`answers record FILE` keeps an answers file under a revise or rewrite run's
`artifact/` as the operator's decisions, in that run's answers/, after the
validator accepts it. Recording a file again after a change, such as an
added `resolution`, replaces the record. `decisions` lists kept answers, and
later runs on the same note receive their decided items.

`run rewrite NOTE --commission FILE` rewrites one note from its authorized
sources when its claims or synthesis are unsettled (see
`commonplace.lib.review_workflows.rewrite`). The commission is Markdown with
YAML frontmatter naming `note` and `sources` (each a `path` and a `role`)
and the section Current direction. A note without a write brief also needs
the sections Intended contribution, Must keep, Must exclude and Reserved
decisions; with a brief they are optional and hold only what the rewrite
adds to it. One writer drafts from the sources and old note. Both writer
and reviewer receive incoming citation passages and earlier decisions.
A typed review judges the exact candidate: fail takes one repair;
warn or pass accepts it. The run always holds its accepted candidate, as `run revise`
holds one with a new warning; `publish RUN` publishes it. When the operator
publishes exactly the judged candidate, the review becomes the note's
current result, so `run revise --triage` presents its `warn` findings.
`--profile` names the worker profile (default: the profile file's `effort`
mapping for `judgment`). It exits 0 when the run ends with a held candidate,
no change or a block and a clean guard, 1 for a stop, a conflict or a guard
change, and 2 when the command failed.

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
from dataclasses import asdict
from pathlib import Path

from commonplace.headless.harness import HARNESSES, Profile
from commonplace.headless.jobs import RunLocked, acknowledge_stopped, dismiss, run_lock
from commonplace.lib import answers, frontmatter
from commonplace.lib.review_workflows import (
    criteria,
    decisions,
    edit_operations,
    edits,
    fixtures,
    gates,
    inbound,
    observations,
    result_contract,
    results,
    revise,
    rewrite,
)
from commonplace.lib.tasks import load_profile

SWEEP = "sweep.json"
"""The run's profile and options: what a resumed gate sweep reuses, and a record of what any other run used."""


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
    rev.add_argument("--must-keep", action="append", default=[], metavar="CLAIM",
                     help="a claim the passes may not narrow, beyond the write brief's Must keep; repeat for each")
    mode = rev.add_mutually_exclusive_group()
    mode.add_argument("--plan", type=Path, help="execute this fixed plan without assessment")
    mode.add_argument("--pass", dest="pass_name", metavar="NAME",
                      help="execute a one-entry plan for this edit operation, without assessment")
    mode.add_argument("--finding", metavar="RESULT",
                      help="execute a one-entry plan that fixes this review result of the artifact, without assessment")
    mode.add_argument("--answers", action="append", metavar="FILE",
                      help="apply the operator's decided answers file: over a per-item pass's proposals, or over "
                      "review results such as a triage's (repeat for each); naming it approves it")
    mode.add_argument("--assess", action="store_true", help="opt into assessment and automatic pass selection")
    mode.add_argument("--triage", action="store_true", help="write a pending answers file over each fresh warn "
                      "or fail review result and end; no review and no assessor")
    mode.add_argument("--full", action="store_true", help="run every review operation that declares a depth, "
                      "then assess with the findings")
    for effort in edit_operations.EFFORTS:
        rev.add_argument(f"--profile-{effort}", help=f"profile for {effort} passes (default: the profile file's "
                         f"`effort` mapping)")
    rev.add_argument("--timeout", type=float, help="seconds a launch may take")
    rw = workflows.add_parser("rewrite", help="rewrite one note from its authorized sources under a commission")
    rw.add_argument("artifact")
    rw.add_argument("--commission", type=Path, metavar="FILE", required=True, help="the commission")
    rw.add_argument("--profile", help="worker profile for every call (default: the profile file's `effort` mapping "
                    "for `judgment`)")
    rw.add_argument("--timeout", type=float, help="seconds a launch may take")
    publish = commands.add_parser("publish", help="publish the candidate a revise or rewrite run held, on the "
                                  "operator's word; launches nothing")
    publish.add_argument("run", type=Path, help="the run directory")
    publish.add_argument("--revised", type=Path, metavar="FILE",
                         help="publish this full revised text of the candidate instead, from a file outside the "
                         "run's artifact/")
    recorded = commands.add_parser(
        "record", help="write a pending answers file over each warn or fail review result a revise run holds, for "
        "the operator's decisions; launches nothing, plans nothing, publishes nothing")
    recorded.add_argument("run", type=Path, help="the revise run directory")
    retry = commands.add_parser("retry", help="dismiss a job's worker problems, or one answer, in a gate sweep run, "
                                "so `run gates --resume` asks again; revise and rewrite runs are never rerun")
    retry.add_argument("run", type=Path)
    retry.add_argument("job", help="the job name: a pair's `<note>::<criterion-id>`")
    retry.add_argument("--key", help="the answer to dismiss; otherwise the worker problems")
    acknowledge = commands.add_parser(
        "acknowledge", help="record that an unsettled worker launch has stopped; check the process first")
    acknowledge.add_argument("run", type=Path)
    acknowledge.add_argument("launch")
    answered = commands.add_parser("answers", help="create an answers file for a question, or record one")
    answer_commands = answered.add_subparsers(dest="answers_command", required=True)
    create_answers = answer_commands.add_parser(
        "create", help="write the answers file for a question, every item pending; launches nothing")
    create_answers.add_argument("--from", dest="question", required=True,
                                help="the question: an edit result with outcome proposed, a review result with "
                                "outcome warn or fail, or a text to approve")
    create_answers.add_argument("--to", help="where to write it (default: <question stem>-answers.md beside "
                                "the question); an existing file is never replaced")
    record_answers = answer_commands.add_parser(
        "record", help="keep an answers file of a revise or rewrite run that nothing consumes as the operator's "
        "decisions; launches nothing")
    record_answers.add_argument("file", help="the answers file, under the run's artifact/")
    listed = commands.add_parser("decisions", help="list operator and agent decisions from the answers runs kept, "
                                 "their publications and pending stops, and the records of the retired "
                                 "procedures; read-only, computes no statistic")
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
        for pair in wanted:
            if pair.kind in criteria.SUPPLIED:
                raise ValueError(f"{pair.kind} has no current result: its freshness is unassessed; "
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
    return gates.new_run_dir(root / gates.RUNS)


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
        if not supplied and [pair.kind for pair in wanted] == [criteria.ROLE]:   # the role report collects its own
            supplied = {inbound.INPUT: inbound.supplied(root, wanted[0].note)}
        observations.atomic_json(run_dir / SWEEP, {**options, "selection": selection})
    operational = bool(arguments.input) or any(pair.kind in criteria.SUPPLIED for pair in wanted)
    report = gates.sweep(root, wanted, profile, run_dir, max_workers=arguments.max_workers or 4,
                         timeout=arguments.timeout,
                         force=arguments.force or bool(arguments.criterion_file) or operational,
                         grouping=arguments.grouping, harnesses=harnesses,
                         publish_results=not bool(arguments.criterion_file) and not operational,
                         operational_inputs=supplied)
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


def _revise(root: Path, arguments: argparse.Namespace, harnesses) -> int:
    artifact = _note(root, arguments.artifact)
    if not artifact.endswith(".md"):
        raise ValueError(f"not a markdown artifact: {artifact}")
    named_plan, focused = None, arguments.pass_name is not None or arguments.finding is not None
    consumed, given, finding_answers = [], {}, {}
    if arguments.plan:
        named_plan = arguments.plan.read_text(encoding="utf-8")   # a missing file is an error, not an assessment
    elif focused:
        finding = None
        if arguments.finding is not None:
            raw = Path(arguments.finding)
            finding = revise.read_finding(root, artifact, (raw.resolve().relative_to(root) if raw.is_absolute()
                                                           else raw).as_posix()).path
        named_plan = revise.one_entry_plan(revise.FIX if finding else arguments.pass_name, finding,
                                           arguments.purpose, arguments.must_keep)
    elif arguments.answers:
        for name in arguments.answers:
            path = observations.safe_path(root, name)
            consumed.append({"origin": path.relative_to(root).as_posix(), "text": path.read_text(encoding="utf-8")})
        named_plan, given, finding_answers = revise.answers_plan(root, artifact, consumed, arguments.purpose,
                                                                 arguments.must_keep)
    if named_plan is not None:
        revise.read_plan(named_plan, root, artifact)
    mode = ("answers" if consumed else "fixed-plan" if named_plan is not None else "assess" if arguments.assess
            else "full" if arguments.full else "triage" if arguments.triage else None)
    if mode is None:
        raise ValueError("choose --plan FILE, --pass NAME or --finding RESULT for fixed-plan execution, --answers "
                         "FILE to apply the operator's answers, --triage to decide the stored findings, or --assess "
                         "or --full for planning; a run never chooses work implicitly")
    if arguments.plan and (arguments.purpose is not None or arguments.must_keep):
        raise ValueError("fixed-plan execution takes purpose and must-keep from the plan; edit the --plan input, "
                         "or give them with --pass or --finding")
    names = {effort: getattr(arguments, f"profile_{effort}") for effort in edit_operations.EFFORTS}
    profiles = edit_operations.effort_profiles(root, names)
    review = load_profile(root, None, gates.profiles()) if mode == "full" else None
    run_dir = edits.new_run_dir(root, "revise", artifact)
    observations.atomic_json(run_dir / SWEEP, {
        "format": observations.VERSION, "workflow": "revise", "mode": mode, "purpose": arguments.purpose,
        revise.MUST_KEEP: arguments.must_keep, "plan": named_plan, "answers": [item["origin"] for item in consumed],
        "profiles": {effort: asdict(profile) for effort, profile in profiles.items()},
        "review-profile": asdict(review) if review else None})
    report = revise.revise(root, artifact, profiles, run_dir, purpose=arguments.purpose,
                           must_keep=arguments.must_keep,
                           named_plan=named_plan if mode in ("fixed-plan", "answers") else None,
                           review=review, triage=mode == "triage", consumed=consumed, given=given,
                           finding_answers=finding_answers, timeout=arguments.timeout, harnesses=harnesses)
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.ok else 1


def _rewrite(root: Path, arguments: argparse.Namespace, harnesses) -> int:
    artifact = _note(root, arguments.artifact)
    if not artifact.endswith(".md"):
        raise ValueError(f"not a markdown artifact: {artifact}")
    rewrite.read_commission(root, artifact, arguments.commission.read_text(encoding="utf-8"),
                            brief="brief" in edits.capture_brief(root, artifact,
                                                                 (root / artifact).read_text(encoding="utf-8")))
    profile = (load_profile(root, arguments.profile, gates.profiles()) if arguments.profile is not None
               else edit_operations.effort_profiles(root, {})["judgment"])
    run_dir = edits.new_run_dir(root, rewrite.WORKFLOW, artifact)
    observations.atomic_json(run_dir / SWEEP, {"format": observations.VERSION, "workflow": rewrite.WORKFLOW,
                                               "profile": asdict(profile)})
    report = rewrite.rewrite(root, artifact, run_dir, profile, commission=arguments.commission,
                             timeout=arguments.timeout, harnesses=harnesses)
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.ok else 1


def _publish(root: Path, arguments: argparse.Namespace) -> int:
    """Publish the candidate the named revise or rewrite run held, or the operator's revision of it."""
    run_dir = _run_dir(root, arguments.run)
    workflow, _ = decisions.run_of(root, run_dir / "artifact" / edits.CANDIDATE)
    revised = None if arguments.revised is None else arguments.revised.read_text(encoding="utf-8")
    report = edits.publish_held(root, run_dir, revised, arguments.revised)
    if workflow == rewrite.WORKFLOW:
        report |= rewrite.store_accepted(root, run_dir, report)
    print(json.dumps(report, indent=2))
    return 0


def _answers(root: Path, arguments: argparse.Namespace) -> int:
    if arguments.answers_command == "record":
        print(json.dumps(decisions.record_answers(root, observations.safe_path(root, arguments.file)), indent=2))
        return 0
    question = observations.safe_path(root, arguments.question)
    rel = question.relative_to(root).as_posix()
    target = (observations.safe_path(root, arguments.to) if arguments.to
              else question.with_name(f"{question.stem}-answers.md"))
    if target.exists():
        raise ValueError(f"answers file exists, not replaced: {target.relative_to(root).as_posix()}")
    if target.resolve().is_relative_to((root / results.RESULTS).resolve()):
        raise ValueError(f"an answers file under {results.RESULTS.as_posix()} would be read as a review result; "
                         "give --to a path outside it")
    edits.write_text(target, answers.pending(rel, question.read_bytes()))
    print(json.dumps({"answers": target.relative_to(root).as_posix(), "question": rel}, indent=2))
    return 0


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
            if arguments.workflow == "revise":
                return _revise(root, arguments, harnesses)
            if arguments.workflow == "rewrite":
                return _rewrite(root, arguments, harnesses)
            if arguments.workflow == "edit":
                return _edit(root, arguments, harnesses)
            return _gates(root, arguments, harnesses)
        if arguments.command == "decisions":
            return _decisions(root, arguments)
        if arguments.command == "answers":
            return _answers(root, arguments)
        if arguments.command == "publish":
            return _publish(root, arguments)
        run_dir = _run_dir(root, arguments.run)
        if arguments.command == "record":
            print(json.dumps(revise.record(root, run_dir), indent=2))
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
