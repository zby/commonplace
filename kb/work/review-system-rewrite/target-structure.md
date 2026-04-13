# Target structure for a review system rewrite

## Organizing principle

Current code is organized by **entry point** (bundle runner, gate-sweep runner, selector, sweep). Each entry point contains the same pipeline stages — target resolution, prompt construction, runner invocation, parsing, finalization — differing mostly in batching shape and execution modality.

The target structure organizes by **layer of concern**. Each layer has a clear dependency direction: domain has no dependencies; protocol depends on domain; provenance depends only on git; persistence depends on domain; orchestration composes everything; integrations adapt review-owned behavior to core protocols; CLI is a thin shell.

## Layer layout

```
commonplace/review/
├── domain/                    pure, no IO
│   ├── snapshots.py           NoteSnapshot, GateSnapshot, AcceptanceSnapshot (frozen value objects)
│   ├── staleness.py           classify_staleness(target, acceptance) -> Staleness
│   ├── applicability.py       gate_applies_to_note(gate, note)
│   ├── trivial_change.py      is_trivial_change(before, after, watched_fields)
│   ├── coverage.py            validate_gate_coverage(requested, received)
│   └── acceptance.py          acceptance kind helpers for each write path
│
├── protocol/                  LLM wire format — sole owner
│   ├── prompt.py              render_prompt(targets, link_table) -> str
│   ├── parser.py              parse_output(text, expected_gates) -> list[ParsedGateReview]
│   ├── format.py              sentinels, result-line grammar, findings extraction
│   └── decisions.py           best-effort decision extraction from review text
│
├── provenance/                git IO, isolated
│   ├── git.py                 blob_sha, file_text_at, last_commit_for_path
│   └── loader.py              SnapshotLoader: batch-capture snapshots, cache within operation
│
├── runners.py                 narrow runner result contract around existing subprocess code
│
├── persistence/               thin SQL, rows in / rows out
│   ├── schema.sql
│   ├── db.py                  connect, ensure_db, transaction context manager
│   └── repos.py               RunRepo, RunGateRepo, ReviewRepo, AcceptanceRepo, NotePathRepo — plain CRUD
│
├── orchestration/             composes the layers
│   ├── targeting.py           Selector: stale pairs, optional diffs
│   ├── planning.py            Planner: stale pairs -> list[ReviewPlan]
│   ├── execution.py           Executor: plan -> prompt -> runner -> parse -> finalize
│   ├── finalization.py        Finalizer: atomic write of run + reviews + acceptances
│   ├── ack.py                 trivial-change auto-ack pass
│   └── sweep.py               multi-plan parallel driver
│
├── integrations/              adapters for non-review core protocols
│   └── relocation.py          ReviewRelocationHook: export moves + DB path rekeys
│
└── cli/                       argparse + prepare_db + one orchestration call
    └── ...
```

## Layer details

### domain/ — pure logic, no IO

Value objects and business rules that can be unit-tested with no mocks.

**snapshots.py**

```python
@dataclass(frozen=True)
class NoteSnapshot:
    path: Path
    blob_sha: str
    commit: str | None   # None = worktree (uncommitted)
    text: str            # loaded once by SnapshotLoader

@dataclass(frozen=True)
class GateSnapshot:
    id: str              # e.g. "prose/source-residue"
    blob_sha: str
    commit: str
    watches: frozenset[str]       # {"body", "title", "description"}
    requires_trait: str | None
    requires_type: str | None
    body: str

@dataclass(frozen=True)
class AcceptanceSnapshot:
    note_path: Path
    gate_id: str
    model_id: str
    accepted_note_sha: str
    accepted_gate_sha: str
```

These replace the bare `(sha, commit)` tuples that currently flow through five modules. A snapshot is captured once and threaded through the pipeline.

**staleness.py**

```python
def classify_staleness(
    note: NoteSnapshot,
    gate: GateSnapshot,
    acceptance: AcceptanceSnapshot | None,
) -> Staleness | None:
    """Returns None if fresh, or a Staleness(reason=...) if stale."""
```

One function, one place. Both targeting and warn-queue filtering call this. Persistence rows are converted to `AcceptanceSnapshot` before entering the domain layer; `domain/` does not import repo row classes.

**trivial_change.py**

```python
def is_trivial_change(
    before_text: str,
    after_text: str,
    watched_fields: frozenset[str],
) -> bool:
    """True if changes are confined to unwatched fields."""
```

Pure text comparison. No git calls, no DB calls. The orchestration layer provides the texts.

### protocol/ — the LLM wire format

Single owner of the sentinel-delimited format. Prompt builder and parser share the same constants.

**prompt.py** renders prompts for both shapes:

```python
def render_bundle_prompt(
    note: NoteSnapshot,
    gates: list[GateSnapshot],
    link_table: dict[str, str],
) -> str: ...

def render_sweep_prompt(
    gate: GateSnapshot,
    notes: list[NoteSnapshot],
    link_tables: dict[Path, dict[str, str]],
) -> str: ...
```

Two functions, not two modules. They share the same sentinel constants and gate-instruction formatting from format.py.

**parser.py** parses output for both shapes:

```python
def parse_bundle_output(
    text: str,
    expected_gate_ids: list[str],
) -> list[ParsedGateReview]: ...

def parse_sweep_output(
    text: str,
    expected_note_paths: list[Path],
    expected_gate_id: str,
) -> dict[Path, ParsedGateReview]: ...
```

**decisions.py** — best-effort decision extraction:

```python
def extract_decision(review_text: str) -> ReviewDecision:
    """Best-effort extraction. Returns 'unknown' on failure.
    
    This is intentionally fuzzy. LLM output is template-guided
    but not rigidly constrained. Losing a review to bad formatting
    is acceptable — the cost of forcing structured output (JSON)
    degrades LLM review quality.
    """
```

The regex chain stays, but lives in one file alongside the format constants it matches against. Legacy import patterns move to a migration utility.

### provenance/ — git IO, isolated

**loader.py** provides batch-friendly snapshot construction:

```python
class SnapshotLoader:
    """Captures note and gate snapshots with internal caching.
    
    One loader per operation. Avoids the current pattern of
    calling git_blob_sha per note per gate in nested loops.
    """
    def __init__(self, repo_root: Path): ...
    def note_snapshot(self, path: Path) -> NoteSnapshot: ...
    def gate_snapshot(self, gate_id: str) -> GateSnapshot: ...
    def note_text_at(self, sha: str, commit: str | None) -> str | None: ...
```

Caching is natural: a loader instance holds a dict of already-resolved SHAs. The current code calls `git_blob_sha` per note per gate in a loop; the loader amortizes this.

### runners.py — narrow runner boundary

Keep this deliberately small at first. The current `review_runners.py` is messy, but much of the mess is real runner-specific operational detail: subprocess spawning, stream handling, session-log matching, and telemetry extraction. Splitting that across several files before the pipeline and persistence boundaries are clean would move complexity more than reduce it.

The useful boundary is the shape orchestration receives:

```python
@dataclass
class RunnerResult:
    output: str                     # the review text
    telemetry: dict | None          # token counts, model, etc.
    actual_model_id: str | None     # may differ from requested

Runner = Callable[[str], RunnerResult]
```

Subprocess execution can stay in one runner module until there is concrete pressure to split it: a third runner, recurring telemetry bugs, or tests that are blocked by the current file shape. The orchestration layer should depend on `RunnerResult`, not on Claude/Codex session-log details.

Live-agent is not primarily a runner implementation. It is a suspended pipeline: create the run and prompt now, then resume at parse/finalize when the agent-produced bundle is ingested.

```python
@dataclass(frozen=True)
class LiveAgentPrompt:
    run_id: int
    prompt_path: Path
```

The key insight: live-agent isn't a different review shape — it's the same pipeline that suspends after prompt rendering and resumes at parsing. Subprocess execution returns a `RunnerResult` immediately; live-agent returns a prompt artifact tied to an existing run id that the ingest CLI uses to resume.

### persistence/ — thin SQL

**repos.py** — plain CRUD, no business rules:

```python
class RunRepo:
    def insert(self, conn, ...) -> int: ...
    def complete(self, conn, run_id, ...) -> None: ...
    def fail(self, conn, run_id, ...) -> None: ...
    def rekey_model(self, conn, run_id, model_id) -> None: ...

class RunGateRepo:
    def insert_many(self, conn, run_id, gates) -> None: ...
    def load_for_run(self, conn, run_id) -> list[RunGateRow]: ...

class ReviewRepo:
    def insert(self, conn, ...) -> int: ...
    def load_for_run(self, conn, run_id) -> list[GateReviewRow]: ...
    def load_for_note(self, conn, note_path) -> list[GateReviewRow]: ...

class AcceptanceRepo:
    def append(self, conn, ...) -> int: ...
    def current_acceptances(self, conn) -> dict[tuple, AcceptanceRow]: ...
    def effective_reviews_with_warns(self, conn) -> list[WarnReviewRow]: ...

class NotePathRepo:
    def count_records(self, conn, note_path: str) -> NotePathRecordCounts: ...
    def rekey(self, conn, old_note_path: str, new_note_path: str) -> None: ...
```

No coverage validation, no model-rekey decisions, no auto-acceptance in the DB layer. Repo methods return row DTOs and perform requested row updates. The targeting/orchestration layer maps `AcceptanceRow` into domain `AcceptanceSnapshot` before calling staleness logic, preserving dependency direction. The current `record_and_finalize_run` splits into: orchestration decides what to write, persistence writes it atomically. `review_run_gates` remains a first-class execution table: it captures the requested gate set before prompt rendering, and ingest/finalization load it as the expected gate contract for an existing run.

**db.py** provides a transaction context:

```python
@contextmanager
def transaction(conn):
    """Single commit point. Orchestration opens one transaction
    per finalization. If any step fails, everything rolls back."""
```

This eliminates the current "cliff" where half the writes succeed before an error.

### orchestration/ — the pipeline

**planning.py** unifies bundle and gate-sweep:

```python
@dataclass
class ReviewPlan:
    shape: PromptShape              # BUNDLE or SWEEP
    targets: list[ReviewTarget]     # (note_snapshot, gate_snapshot) pairs
    model_id: str

class Planner:
    def plan_bundle(self, note: NoteSnapshot, gates: list[GateSnapshot], model_id: str) -> ReviewPlan: ...
    def plan_sweep(self, gate: GateSnapshot, notes: list[NoteSnapshot], model_id: str) -> ReviewPlan: ...
    def plan_from_stale(self, stale_pairs, strategy: str) -> list[ReviewPlan]: ...
```

"Bundle" and "gate-sweep" are two ways to group the same stale pairs into plans. The Executor doesn't care which.

**execution.py** — one pipeline:

```python
class Executor:
    def execute_subprocess(self, plan: ReviewPlan, runner: Runner) -> ExecutionResult:
        """plan -> create run -> prompt -> runner -> parse -> finalize existing run"""
        run_id = self.finalizer.create_running_run(plan)
        prompt = self.protocol.render(plan, run_id=run_id)
        result = runner(prompt)
        parsed = self.protocol.parse(result.output, plan)
        return self.finalizer.finalize_existing_run(
            run_id,
            parsed,
            telemetry=result.telemetry,
            actual_model_id=result.actual_model_id,
        )

    def create_live_agent_prompt(self, plan: ReviewPlan) -> LiveAgentPrompt:
        """Create a run and prompt artifact, then suspend until ingest."""
        run_id = self.finalizer.create_running_run(plan)
        prompt = self.protocol.render(plan, run_id=run_id)
        return self.prompt_writer.write(run_id=run_id, prompt=prompt)

    def resume(self, run_id: int, bundle_text: str) -> ExecutionResult:
        """Resume a suspended live-agent execution at the parse step."""
        run = self.run_repo.require_running(run_id)
        run_gates = self.run_gate_repo.load_for_run(run_id)
        parsed = self.protocol.parse(bundle_text, run_gates, model_id=run.model_id)
        return self.finalizer.finalize_existing_run(run_id, parsed, telemetry=None)
```

The live-agent path reuses the same parse + finalize tail, but it resumes an existing run rather than creating a second run. The run id, reviewed note SHA, requested gate set, and gate SHAs are captured before prompt rendering; ingest loads that captured contract and finalizes the existing run.

**finalization.py** — atomic writes:

```python
class Finalizer:
    def finalize_existing_run(self, run_id, parsed_reviews, telemetry, actual_model_id=None) -> FinalizationResult:
        with transaction(self.conn):
            if actual_model_id is not None:
                self.run_repo.rekey_model(conn, run_id, actual_model_id)
            for review in parsed_reviews:
                self.review_repo.insert(conn, run_id, ...)
                self.acceptance_repo.append(conn, acceptance_kind="full-review", ...)
            self.run_repo.complete(conn, run_id, ...)
        return FinalizationResult(run_id, ...)
```

Gate-coverage validation calls `domain/coverage.py` before review rows or acceptance events are written. Because the run is captured before prompt rendering, parse or coverage failure should mark the existing run failed while keeping gate review inserts and acceptance events all-or-nothing. If runner telemetry reports an actual model partition that differs from the requested partition, model rekeying remains a finalization responsibility: the DB repo performs the row updates, but orchestration decides to apply them before writing reviews and acceptances.

**sweep.py** — parallel driver:

```python
class Sweep:
    def run(self, plans: list[ReviewPlan], runner: Runner, *, max_workers: int = 4):
        """ThreadPoolExecutor over plans. Extracted from cli/review_sweep.py."""
```

Currently this logic lives in the CLI wrapper. Moving it here makes it testable and reusable.

### integrations/ — downstream adapters for core workflows

The base code-structure rewrite introduced `commonplace.lib.relocation.RelocationHook`. Core relocation now plans note path moves and calls hooks without importing review code. The review system implements that hook downstream.

**relocation.py**

```python
class ReviewRelocationHook:
    def plan(self, *, root: Path, moves: Sequence[NotePathMove]) -> ReviewRelocationPlan | None: ...
    def describe(self, plan: ReviewRelocationPlan) -> list[str]: ...
    def execute(self, plan: ReviewRelocationPlan) -> None: ...
```

Responsibilities:

- Move review export directories when note paths change.
- Rewrite legacy ReviewMetadata blocks inside exported review files.
- Rekey review DB rows through the persistence layer.
- Report preflight collisions before core relocation mutates files.

This is an adapter, not a second orchestration pipeline. It exists because core relocation owns markdown link rewriting and file movement, while review owns review exports and review DB state. The dependency direction is non-negotiable: `commonplace.review.integrations.relocation` may import the core hook protocol, but `commonplace.lib.relocation` must never import review code.

## Design rationale

### Why "plan, not mode"

Current code has two orchestrators (`run_review_bundle`, `run_gate_sweep`) that do the same thing differently. The plan abstraction makes the batching strategy a parameter, not a code path. Adding a third shape (e.g., "few gates x few notes") would be a new plan variant and prompt template, not a new orchestrator.

### Why snapshot value objects

Eliminates five modules independently calling provenance functions and threading bare tuples. Caching is free (loader holds a dict). Debug logging of SHAs at each pipeline step becomes trivial.

### Why single protocol module

The LLM wire format is one contract. Currently it's split across prompt builder (in run_review_bundle), sentinel parser (in run_review_bundle and gate_sweep_format), and decision parser (in review_decisions). Changing the output format means touching three files in different locations. With a single protocol module, it's one change.

### Why best-effort parsing matters

Constraint 5 from the README: this is a fuzzy system. Template guidance works well enough in practice. Forcing JSON output from the LLM degrades review quality — the intelligence cost exceeds the parsing reliability gain. The parser should be generous (extract what it can, default to `unknown`) not strict (reject malformed output). This is a deliberate design choice, not an oversight.

### Why thin persistence

The current `record_and_finalize_run` in review_db.py embeds coverage validation, model rekeying, and auto-acceptance. These are business rules that happen to be near the DB — they're not DB concerns. Extracting them into orchestration means the DB layer can be a simple, testable CRUD boundary, and the business rules can be tested with no DB.

### Why the live-agent path is a suspended pipeline, not a separate shape

The live-agent path currently works as three separate CLI commands (create-run, agent-follows-prompt, ingest-bundle-output). Conceptually it's the same pipeline as subprocess — it just suspends between prompt rendering and output parsing. Modeling it this way means the ingest command calls `Executor.resume`, reusing the same parse -> finalize tail. No duplicate finalization logic.

## What this buys

1. **One parser, one emitter.** LLM contract changes touch one module.
2. **One pipeline, two shapes.** Adding a new batching strategy is adding a plan variant, not a new orchestrator.
3. **Runner complexity is contained.** Orchestration receives a small `RunnerResult` and does not know about session logs or telemetry heuristics.
4. **Pure domain is unit-testable.** Staleness, coverage, trivial-ack — all pure functions on value objects.
5. **DB layer stays under ~400 lines.** Down from 910.
6. **Finalization cliffs vanish.** Review rows and acceptance events commit together; parse or coverage failure marks the existing run failed without partial acceptance state.
7. **Warn queue collapses.** A query in repos.py + findings extraction in protocol/format.py. No separate orchestrator.
8. **Core/review coupling stays inverted.** Review-owned adapters plug into core protocols without making the core package depend on review.

## Open questions

- **Should `Executor` be a class or a function?** Class carries injected dependencies (protocol, finalizer, repos, prompt writer). Function takes them as arguments. Class is more natural for the live-agent suspend/resume pattern.
- **How to handle the existing legacy decision regexes?** Move to a one-off migration utility, or keep in protocol/decisions.py behind a `legacy=True` flag? Probably keep a reduced set in the main parser (some are still useful as fallbacks) and move import-specific patterns to a migration tool.
- **Should `SnapshotLoader` batch git calls?** Currently each `git_blob_sha` call is a subprocess. Batching via `git cat-file --batch` would be faster for sweeps over many notes. Worth it only if profiling shows it matters.
- **How long should review exports survive?** `ReviewMetadata` block parsing is now active only because exported review markdown has to move with notes. If exports become regenerable or deprecated, the relocation integration can drop that branch and keep only DB rekeying.
