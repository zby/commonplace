# Target structure for a review system rewrite

## Organizing principle

Current code is organized by **entry point** (bundle runner, gate-sweep runner, selector, sweep). Each entry point contains the same pipeline stages — target resolution, prompt construction, runner invocation, parsing, finalization — differing only in batching shape and runner strategy.

The target structure organizes by **layer of concern**. Each layer has a clear dependency direction: domain has no dependencies; protocol depends on domain; provenance depends only on git; persistence depends on domain; orchestration composes everything; CLI is a thin shell.

## Layer layout

```
commonplace/review/
├── domain/                    pure, no IO
│   ├── snapshots.py           NoteSnapshot, GateSnapshot (frozen value objects)
│   ├── staleness.py           classify_staleness(target, acceptance) -> Staleness
│   ├── applicability.py       gate_applies_to_note(gate, note)
│   ├── trivial_change.py      is_trivial_change(before, after, watched_fields)
│   ├── coverage.py            validate_gate_coverage(requested, received)
│   └── acceptance.py          decide_acceptance_kind(decision) -> AcceptanceKind
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
├── runners/                   strategies behind one interface
│   ├── base.py                Runner protocol + RunnerResult + RunContext
│   ├── subprocess_claude.py   claude-code runner
│   ├── subprocess_codex.py    codex runner
│   └── live_agent.py          writes prompt file, returns handle for later ingest
│
├── persistence/               thin SQL, rows in / rows out
│   ├── schema.sql
│   ├── db.py                  connect, ensure_db, transaction context manager
│   └── repos.py               RunRepo, ReviewRepo, AcceptanceRepo — plain CRUD
│
├── orchestration/             composes the layers
│   ├── targeting.py           Selector: stale pairs, optional diffs
│   ├── planning.py            Planner: stale pairs -> list[ReviewPlan]
│   ├── execution.py           Executor: plan -> prompt -> runner -> parse -> finalize
│   ├── finalization.py        Finalizer: atomic write of run + reviews + acceptances
│   ├── ack.py                 trivial-change auto-ack pass
│   └── sweep.py               multi-plan parallel driver
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
```

These replace the bare `(sha, commit)` tuples that currently flow through five modules. A snapshot is captured once and threaded through the pipeline.

**staleness.py**

```python
def classify_staleness(
    note: NoteSnapshot,
    gate: GateSnapshot,
    acceptance: AcceptanceRecord | None,
) -> Staleness | None:
    """Returns None if fresh, or a Staleness(reason=...) if stale."""
```

One function, one place. Both targeting and warn-queue filtering call this.

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

### runners/ — strategy pattern

**base.py** defines the protocol:

```python
class Runner(Protocol):
    def run(self, prompt: str, ctx: RunContext) -> RunnerResult: ...

@dataclass
class RunnerResult:
    output: str                     # the review text
    telemetry: dict | None          # token counts, model, etc.
    actual_model_id: str | None     # may differ from requested
```

Subprocess runners implement this with spawn + stream + telemetry extraction. Each runner's telemetry logic stays local to its module — that complexity is real and runner-specific, not abstractable.

**live_agent.py** models the "suspend and resume" pattern:

```python
class LiveAgentRunner:
    """Writes prompt to a file and returns a handle.
    
    The current agent follows the prompt and writes the bundle artifact.
    A subsequent ingest command calls Executor.resume(handle, bundle_text)
    to complete the parse -> finalize tail of the pipeline.
    """
    def run(self, prompt: str, ctx: RunContext) -> LiveAgentHandle: ...
```

The key insight: live-agent isn't a different pipeline — it's the same pipeline that suspends after prompt rendering and resumes at parsing. The Executor handles both: subprocess runners return a `RunnerResult` immediately; live-agent returns a handle that the ingest CLI uses to resume.

### persistence/ — thin SQL

**repos.py** — plain CRUD, no business rules:

```python
class RunRepo:
    def insert(self, conn, ...) -> int: ...
    def complete(self, conn, run_id, ...) -> None: ...
    def fail(self, conn, run_id, ...) -> None: ...

class ReviewRepo:
    def insert(self, conn, ...) -> int: ...
    def load_for_run(self, conn, run_id) -> list[GateReviewRow]: ...
    def load_for_note(self, conn, note_path) -> list[GateReviewRow]: ...

class AcceptanceRepo:
    def append(self, conn, ...) -> int: ...
    def current_acceptances(self, conn) -> dict[tuple, AcceptanceRecord]: ...
    def effective_reviews_with_warns(self, conn) -> list[...]: ...
```

No coverage validation, no model rekeying, no auto-acceptance in the DB layer. The current `record_and_finalize_run` splits into: orchestration decides what to write, persistence writes it atomically.

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
    def execute(self, plan: ReviewPlan, runner: Runner) -> ExecutionResult:
        """plan -> prompt -> runner -> parse -> finalize"""
        prompt = self.protocol.render(plan)
        result = runner.run(prompt, ctx)
        parsed = self.protocol.parse(result.output, plan)
        return self.finalizer.finalize(plan, parsed, result.telemetry)

    def resume(self, handle: LiveAgentHandle, bundle_text: str) -> ExecutionResult:
        """Resume a suspended live-agent execution at the parse step."""
        parsed = self.protocol.parse(bundle_text, handle.plan)
        return self.finalizer.finalize(handle.plan, parsed, telemetry=None)
```

The live-agent path reuses the same parse + finalize tail. No duplicate pipeline.

**finalization.py** — atomic writes:

```python
class Finalizer:
    def finalize(self, plan, parsed_reviews, telemetry) -> FinalizationResult:
        with transaction(self.conn):
            run_id = self.run_repo.insert(...)
            for review in parsed_reviews:
                self.review_repo.insert(conn, run_id, ...)
                kind = decide_acceptance_kind(review.decision)
                self.acceptance_repo.append(conn, ...)
            self.run_repo.complete(conn, run_id, ...)
        return FinalizationResult(run_id, ...)
```

Gate-coverage validation calls `domain/coverage.py` before the transaction opens. If coverage fails, nothing is written.

**sweep.py** — parallel driver:

```python
class Sweep:
    def run(self, plans: list[ReviewPlan], runner: Runner, *, max_workers: int = 4):
        """ThreadPoolExecutor over plans. Extracted from cli/review_sweep.py."""
```

Currently this logic lives in the CLI wrapper. Moving it here makes it testable and reusable.

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
3. **Runners are pluggable.** Adding a third runner is implementing `Runner.run`.
4. **Pure domain is unit-testable.** Staleness, coverage, trivial-ack — all pure functions on value objects.
5. **DB layer stays under ~400 lines.** Down from 910.
6. **Finalization cliffs vanish.** One transaction, or nothing.
7. **Warn queue collapses.** A query in repos.py + findings extraction in protocol/format.py. No separate orchestrator.

## Open questions

- **Should `Executor` be a class or a function?** Class carries injected dependencies (protocol, finalizer, repos). Function takes them as arguments. Class is more natural for the live-agent suspend/resume pattern.
- **How to handle the existing legacy decision regexes?** Move to a one-off migration utility, or keep in protocol/decisions.py behind a `legacy=True` flag? Probably keep a reduced set in the main parser (some are still useful as fallbacks) and move import-specific patterns to a migration tool.
- **Should `SnapshotLoader` batch git calls?** Currently each `git_blob_sha` call is a subprocess. Batching via `git cat-file --batch` would be faster for sweeps over many notes. Worth it only if profiling shows it matters.
