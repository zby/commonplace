# Batch 21 correction helper: current-code compatibility review

**Outcome: the prepared helper remains blocked by its source-byte guard. The
reset implementation and all five runtime-file seals match, but that does not
make the two changed modules unreachable or establish behavioral equivalence.**
This is an independent read-only review, not release authority. No reset,
judgment, advance, preparation, acquisition, installation, launch, integration
or commit was performed. Only this report was written. Writer exclusion and
all-nine launch readiness are not assessed.

## Evidence boundary

Reviewed the complete [correction README](./batch-21-corrections/README.md),
[plan](./batch-21-corrections/plan.json) (2,938 lines), and
[helper](./bash-21-corrections.sh). Compared
`f12f9a7467f4b01a5777bf8f65f109560b05e848..67482d6cf903522dd6313f51c56eeeba26c3fd1d`
with the exact command:

```text
git diff f12f9a746..HEAD -- src/commonplace pyproject.toml uv.lock
```

There are exactly two changed files, 52 insertions and 18 deletions:
`src/commonplace/lib/systems_matrix.py` and
`src/commonplace/lib/agentic_analysis/rules.py`. Neither dependency manifest nor
lockfile changed. The working package/dependency paths also had no diff against
HEAD when checked. Unrelated workshop and ingest changes were left untouched.

Read the direct and conditional paths below. For the nine historical run
identities, inspected only recorded library roots and code-handler declarations
from `run.json`, not analytical prompts, logs or target repositories. All nine
use the standard check/application/assembly/publication handler families. The
parent and another worker own the separate test and dispatched-method reviews;
this report does not substitute for them or report their tests as run here.

Citations below are repository-relative paths with current-HEAD line numbers,
unless a historical revision is explicitly named. Confidence is **high** for
byte comparisons and static call paths; execution outcomes remain conditional
because no state transition or analytical execution was permitted.

## 1. The immediate blocker is intentional and reproducible

The helper imports origin `publication` and checks its location before the
package-wide equality test (`bash-21-corrections.sh:70–75`). That test compares
`src/commonplace`, `pyproject.toml` and `uv.lock` against `reset-code-commit`.
The two-file diff necessarily produces `Reset code/dependencies changed` before
any per-case preflight or native reset. This conclusion does not require running
the helper or inspecting its targets. The guard checks the working tree against
the pinned commit, not merely whether changes are committed.

Independently computed SHA-256 of each `runtime-files` path and the launcher:
all six matched the manifest. The five runtime paths are `artifactrun/reset.py`,
`artifactrun/run.py`, `artifactrun/engine.py`, `artifactrun/store.py`, and
`lib/agentic_analysis/publication.py`. The exact Git diff confirms they are
unchanged since the reset pin. These are **positive seal checks, not a complete
transitive dependency seal**. The broad guard currently covers the gap.

## 2. Reachability: distinguish importing code from invoking changed logic

| Phase | Python implementation used | Reachability of the changed modules |
| --- | --- | --- |
| Helper startup, including `--check` | Origin package, explicitly checked | Both imported: `publication.py:43` imports `validation`; `validation.py:2080–2081` imports/registers `agentic_analysis.rules`; `rules.py:53` imports `systems_matrix.profile_member_comparison`. This occurs before the failing equality guard. |
| Preflight `Run` and `affected_jobs` | Origin | Run interpretation and dependency computation do not invoke comparison validation (`run.py:72–89`; `reset.py:41–94`). |
| External `reset_run`, if later authorized and admitted | Origin | Reset dynamically imports affected code-handler modules, including checks and publication (`reset.py:172–181`). Both changed modules are in that import closure. The standard reset hooks do not call their changed comparison logic. |
| Native `judge`, driver advancement and inspection | Each prepared worktree's local package, if its command environment binds as intended | The same validation families are reachable in the frozen package. They are not automatically replaced by current-origin modules. Mere imports during CLI startup are not validation execution. |
| Later candidate checks, assembly, publication | Frozen handler implementations and their imported rules | Comparison validation is executed in these families. Publication also validates the inherited retained corpus through destination inspection. This is behavior-sensitive, not just an import dependency. |

### External reset's actual effect path

`reset_run` loads run state, checks open/uncertain attempts and computes the
forward dependency closure (`reset.py:143–171`). For affected code jobs it
looks up a sibling `reset_<handler>` hook (`172–181`); it does **not** invoke
ordinary check, assembly or publication handlers to obtain their normal outputs.
The inspected declarations use those standard families. The publication hook
is `publication.reset_publish_analysis` (`publication.py:303–376`).

Its preparation reads opening metadata and preparation identity, checks that
the run has not already been integrated, and reconciles destination/archive
maps with the journal (`publication.py:324–372`). It returns replacements for
the unreleased publication, journal and any incumbent archive. It does not call
`_prepare_publication`, `inspect_destination`, `current_analyses`,
`validate_pinned_artifact_snapshot`, or `profile_member_comparison`.

Reset snapshots run state and effect replacements before mutation, removes
retired attempts/judgments, records the budget floor, rematerializes the working
artifact, and applies replacements under the pending-reset marker
(`reset.py:183–257`). `_materialize` copies interpreted member bytes and a
minimal manifest; it does not validate profile coverage
(`engine.py:462–481`). Nothing in the two-file patch changes this algorithm or
its publication-withdrawal hook. Static confidence is high that the **changed
comparison branches are not invoked by this standard reset effect path**.
It would be incorrect to say the changed files are not loaded by reset.

### Cwd, library overrides and delayed imports do not switch Python packages

`Run.library` comes from the recorded run metadata (`run.py:85`); all nine
record their own worktree's `kb`. Separately, `library_root` can choose a library
from cwd or `COMMONPLACE_LIBRARY_ROOT` (`library.py:87–110`). Validation can
supply member/manifest/criterion bytes in memory (`validation.py:1621–1694`,
`1998–2077`). These select data and contracts, not Python implementations.
Changing cwd, supplying closed criterion bytes, or pointing the library at an
old worktree does not unload the origin rules or change the package's module
search path. No such override in the helper makes its origin imports frozen.

This matters for imports delayed until handler dispatch:
`CodeJob.resolve_handler` uses `importlib` (`plan.py:53–58,113–117`), and
`engine.py:543` invokes the resolved handler. Reset uses its own delayed import
at `reset.py:178`. The loaded package binding, not the handler string's age or
the run's stored library, determines the implementation imported. In the
external helper that binding is origin; in properly bound native subprocesses
it is the frozen worktree. No cross-package substitution was observed in the
helper source.

Native CLI execution is additionally fenced by `require_run_code`
(`cli/run.py:152–155`; `artifactrun/worktree.py:178–205`), which checks both
loaded package root and cwd. Publication's opened-method guards also require
the executing source to match the opened commit (`guards.py:40–56`;
`worktree.py:412–440`). Running current-origin native commands from an old cwd
is therefore neither equivalent nor a supported way around frozen behavior.
External reset deliberately calls the API rather than that native CLI fence;
its own stronger binding checks must remain explicit.

## 3. What the patch changes when validation actually runs

`systems_matrix.py:176–260` changes the meaning of classified coverage:

- A warranted local `trace_learning: no` now counts as a classified finding.
  It still requires a `known` unit and an absence-record reference.
- A partial axis can now consist of classified local negatives plus unresolved
  coverage. Conversely, an unclassified axis carrying a local negative is
  rejected under ordinary current rules. Previously local negatives were left
  out of the positive-findings accumulator, so these two cases behaved
  differently.
- The projection is unchanged: under incomplete coverage or a positive witness,
  local `no` is suppressed from the system-level existence union
  (`systems_matrix.py:275–293`). This is not a forced system-wide negative.
- A new optional `retained_content` parameter and private historical flag are
  additive at the call interface, but alter validation behavior for eligible
  inputs (`systems_matrix.py:166–177,299–314`). Existing two-argument callers
  remain callable. Callable compatibility is not accepted-input equivalence.

Candidate checks call `validate_draft_in_role` through
`artifactrun/checks.py:71–82`. The draft adapter strips manifest member pins
**in memory** (`validation.py:2056–2062`). The new retained exception therefore
does not apply to draft checks, even to an exact historical profile submitted
as a candidate at a retained path. Assembly and publication use a pinned
snapshot with intended path `run_dir/artifact`
(`publication.py:150–159,223–224,252`), not a direct child of `RETAINED_ROOT`.
They likewise do not receive the retained exception through the artifact rule.
The changed strict coverage logic would matter if current rules were substituted
into any of these frozen producer paths.

The new `rules.py:325–334` branch supplies historical bytes only for an artifact
directly under that validation context's retained root with a member-pin map.
The bytes must also hash to one of two fixed profiles and parse to the supplied
metadata (`systems_matrix.py:307–314`). Other checks, record resolution and
manifest validation remain in force. The exception is not a general allowance
for old runs, filenames, copied frontmatter, or new candidates.

## 4. Inherited-corpus validation is a real conditional consumer

Publication's `inspect_incumbent` calls `inspect_destination`
(`publication.py:284–296`). Destination inspection validates **every** current
artifact before selecting its own destination (`guards.py:83–102`).
`current_analyses` loads each via `load_analysis` and `ValidationRun`
(`analyses.py:118–126,186–225`); the registered artifact rule then executes
comparison validation (`validation.py:496–512`; `rules.py:323–334`).
Thus an unrelated inherited profile can stop publication. It is not enough to
check only the corrected system's own profile.

The two historical seals currently match canonical profiles for EchoWiki
(`mohammadmaso--echowiki`, SHA-256 beginning `0712abad`) and Interview Doc Agent
(`shilren--interview-doc-agent`, beginning `a5a82049`). Read-only existence/hash
checks found those exact profiles inherited in the two batch-20 worktrees,
MehmetGoekce LLM Wiki and ClawVault. They were absent at those canonical paths
in the other seven worktrees. This establishes a concrete loading context,
not a hypothetical corpus concern. No analytical body or target source was
needed to establish it.

Both changed local files in each of the nine worktrees match that worktree's
recorded method commit and differ from current origin. For the two batch-20
methods, `git diff fb6ad58f..f12f9a746` is empty for `systems_matrix.py`,
`rules.py`, `guards.py` and `analyses.py`. Consequently their original rules
already allow the historical local-negative/unclassified-axis pattern; merely
remaining frozen does not newly impose current strict rules without their
exception. **Do not backport only the stricter accumulator change** into those
methods: their inherited-corpus publication check is exactly where the two
historical exceptions could become necessary. No frozen-file patch is proposed.

`systems_matrix.load_results` is a separate retained consumer: it first
validates the full current corpus and then passes each selected profile's
published bytes to `profile_member_comparison` (`systems_matrix.py:324–358`).
Reset does not call this matrix loader. Its existence does not prove reset
executes comparison validation; it explains why current retained readers need
the exact-byte exception as well as the registered artifact rule.

## 5. Compatibility meanings and release recommendation

**Source-byte compatibility** means the executing source/dependency inputs equal
the approved baseline. The helper currently requires that property and it is
false, despite the five sealed runtime files matching.

**Interface compatibility** means callers can still invoke the same APIs and
interpret their results. The changed comparison APIs add optional keyword
parameters; reset's API and result structure are unchanged in this diff.
That is encouraging but narrower than behavior compatibility.

**Behavior compatibility** means relevant inputs still produce the same
validation decisions and permitted effects. The comparison patch intentionally
changes decisions, and cannot be called globally behavior-equivalent. For the
standard external reset path, the changed comparison branches are not called;
that narrower static argument does not approve current code for frozen
candidate checks or publication. Nor does it prove all effects under failure,
interruption or a future code change are equivalent.

The least-risk future release should preserve the existing stop now and avoid
changing any frozen producer method or accepting arbitrary newer origin code.
Prefer an explicitly authorized **reset-only execution binding to the original
`f12f9a746` package/dependencies**, separated from the continuing native frozen
commands. A separately prepared, immutable code environment would require a
small, reviewed helper binding change because the current helper insists the
package root and publication hook are in this origin checkout. Retained-origin
identity and integrated-result exclusion must still refer to the true origin,
not accidentally to a runtime checkout. That environment must not create new
analysis runs or change historical worktrees. Preparation/installation and
binding edits require a new commission; none is authorized here.

If the operator instead chooses current origin, the alternative is a narrowly
reviewed reset-only exception for **this exact two-file patch**, while retaining
an exact baseline comparison for every other package/dependency file and the
five existing seals. Such a release must demonstrate the import/effect closure
in disposable tests and bind the approved exception explicitly. It must not
replace `reset-code-commit` with HEAD, refresh stale hashes to make checks green,
ignore all validation files, or extend the exception to native advancement or
publication. This alternative carries more compatibility-review responsibility
than an unchanged reset runtime; this report alone does not clear it.

### Blockers versus follow-ups

- **Current blocker, high confidence:** package-wide source equality fails on
  the two committed changes. Do not launch the existing helper unchanged.
- **Authority blocker:** review grants no execution, binding, launcher or
  environment-preparation authority. A release decision must be separate.
- **Required before a future release:** parent's disposable reset/feedback and
  frozen-dispatch evidence; explicit runtime binding; normal complete guard
  checks; exclusive-writer clearance; source/method/publication identity and
  budget checks. This review establishes none of those live clearances.
- **Follow-up, not an observed reset regression:** test inherited-corpus
  publication under the intended frozen environments, especially both batch-20
  cases; distinguish an existing corpus failure from an introduced validator
  mismatch. Do not inspect or repair the corpus by broadening this commission.
- **Not a blocker established here:** changed comparison semantics breaking the
  standard external withdrawal itself. Static paths show imports but no call to
  the changed validation branches. Execution-level proof is left to the
  separately commissioned disposable tests.

## Report validation

Validation command: `commonplace-validate kb/work/agentic-system-reruns/batch-21-current-code-review.md`.

```text
VALIDATION SUCCESS
Target: kb/work/agentic-system-reruns/batch-21-current-code-review.md
Scope: kb/work/agentic-system-reruns/batch-21-current-code-review.md
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

Broader graph discovery with `cp-skill-connect` is a possible later step,
outside this report's write scope.
