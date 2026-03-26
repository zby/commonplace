# Selector refactor — library core, thin CLI

The selector is becoming an operational primitive, not just a one-off script. The main risk is not missing flags; it is letting inventory, review-state loading, change detection policy, diff generation, and output rendering stay fused in one file.

The current `scripts/notes_selector.py` already shows this pressure:

- inventory is hardcoded to top-level notes
- policy is partially encoded as `frontmatter_only=args.review_type == "frontmatter-review"`
- review metadata resolution and blob loading are interleaved with policy decisions
- diff generation is coupled to change detection
- the CLI owns behavior selection rather than delegating to a selector engine

If we keep extending the current script in place, each new selector mode becomes another conditional branch, and cross-script consistency with `ack_review.py` / `summarize_reviews.py` gets harder.

## Goals

1. Make review-type-specific selection logic a first-class policy, not a boolean.
2. Make selection decisions testable without invoking the full CLI or git I/O stack.
3. Share review path and review-state resolution logic across selector-adjacent scripts.
4. Allow future selectors to vary along multiple axes:
   - inventory scope
   - frontmatter filters
   - staleness thresholds
   - change-detection rules
   - diff style
   - sort / ranking policy
   - output format

## Recommendation

Do not start with recursive scope, new filters, and sorting flags. Start by separating the selector into a small library with explicit data models and a policy registry. Once that exists, new flags become cheap and low-risk.

## Target architecture

### 1. Data model layer

Introduce explicit internal models instead of passing raw paths and loosely-related fields through one function.

Suggested shapes:

```python
@dataclass
class NoteCandidate:
    path: Path
    rel_path: str


@dataclass
class NoteSnapshot:
    path: Path
    rel_path: str
    text: str
    blob_sha: str
    frontmatter_raw: str | None
    body_text: str
    body_lines: list[str]


@dataclass
class ReviewState:
    review_type: str
    review_path: Path | None
    metadata: ReviewMetadata | None
    accepted_blob_sha: str | None
    accepted_snapshot: NoteSnapshot | None
    load_error: str | None


@dataclass
class SelectionDecision:
    status: str
    reason: str
    diff_kind: str
    sort_key: object | None = None
```

These are internal models, not public API contracts.

### 2. Pipeline shape

Refactor selection into explicit stages:

1. `inventory` — find candidate notes
2. `filters` — optional note-level filters before review-state loading
3. `review_state` — locate review file, parse metadata, resolve accepted blob
4. `policy` — decide changed / unchanged and why
5. `diff materialization` — only build diffs if the output mode needs them
6. `render` — paths, json, stats, explain output

This is a better fit than one `build_change_record()` function that does all of the above.

### 3. Policy registry

Replace review-type booleans with a policy registry.

Example:

```python
SELECTOR_POLICIES = {
    "prose-review": prose_review_policy,
    "semantic-review": semantic_review_policy,
    "frontmatter-review": frontmatter_review_policy,
}
```

Or slightly more declarative:

```python
SelectorPolicy(
    name="frontmatter-review",
    rules=[
        missing_review_rule,
        missing_metadata_rule,
        invalid_accepted_blob_rule,
        frontmatter_changed_rule,
        body_rewrite_rule(threshold=0.5),
        unchanged_rule,
    ],
    default_diff_kind="frontmatter",
)
```

This is the core flexibility mechanism. New selectors should mean adding a policy, not editing a long conditional.

### 4. Shared review-path and review-state helpers

Move the canonical review-path mapping out of `notes_selector.py` and into shared code used by:

- `notes_selector.py`
- `ack_review.py`
- `summarize_reviews.py`
- any future review-maintenance scripts

This should include:

- `review_path_for(note_path, review_type, notes_root, reviews_root)`
- `load_review_state(...)`
- accepted-blob resolution
- safe blob reading with structured failure modes

`review_metadata.py` is the most likely home, though it may need to be split into:

- `review_metadata.py` for parsing/rendering metadata
- `review_state.py` for git-backed resolution and snapshot loading

### 5. Diff generation as a separate concern

The policy should decide:

- changed or unchanged
- reason
- preferred `diff_kind`

It should not necessarily build the diff immediately.

Example diff kinds:

- `none`
- `full`
- `frontmatter`
- `body`

This matters because some callers only need note paths, while others want JSON with compact diffs. The current implementation does more work than necessary by coupling decision and diff building.

### 6. Thin CLI

Keep `scripts/notes_selector.py` as the user-facing entry point, but make it a thin wrapper over library functions.

The CLI should do only:

- argument parsing
- call into selector engine
- render output

It should not contain review-type policy logic directly.

## Concrete selector behaviors to support

The architecture should make these selectors easy to express:

- `frontmatter-review`
  - changed if frontmatter changed
  - changed if body rewrite ratio > threshold
- `semantic-review`
  - changed if accepted full text differs
- `prose-review`
  - changed if accepted full text differs
- future `staleness-review`
  - changed if `last-accepted-at` exceeds age threshold
- future `index-review`
  - changed if members changed or outbound link contract drift is detected
- future `current-only` queues
  - inventory/filter concern, not policy concern

## Scope design

Recursive scope is valuable, but it should not be the first architectural move.

Recommendation:

- Keep current top-level-only inventory initially.
- Add explicit scope arguments after the selector engine exists.
- Make recursion opt-in first.

Why:

- review file naming collisions for subdirectory notes are real
- the meaning of "reviewable notes" may differ by directory
- widening scope and refactoring architecture at the same time confounds failures

After the engine exists, add:

- `--dir`
- `--recursive`
- maybe later `--glob` or `--path-prefix`

## Sorting and filtering design

These should be represented as separate post-processing layers, not embedded into policy functions.

### Filters

Filters should operate on `NoteSnapshot` or parsed frontmatter, before expensive review-state loading where possible:

- `--status`
- `--tag`
- `--type`

### Sorting

Sorting should operate on `SelectionDecision` plus optional attached metrics:

- `alpha`
- `oldest-review`
- `most-changed`
- future `highest-risk`

This implies that policies may expose structured metrics, not just strings.

## Test strategy

The refactor should be driven by tests at 3 levels.

### 1. Pure unit tests

No git subprocesses. Test:

- frontmatter comparison
- body rewrite ratio
- individual policy rules
- rule ordering

### 2. Selector-engine tests

Small temp repos. Test:

- missing review
- missing metadata
- unreadable accepted blob
- per-policy changed/unchanged outcomes
- recursive path mapping once added

### 3. CLI tests

Only a thin set:

- argument validation
- json/path output shape
- `--include-unchanged`

The current test file is too selector-script-centric. After refactor, most tests should target library functions.

## Implementation phases

### Phase 1. Extract library

- Move inventory, review-state loading, and rendering helpers into internal functions/modules.
- Keep current top-level-only inventory.
- Keep current three review types only.

Success criterion: cleaner seams without widening scope at the same time.

### Phase 2. Introduce policy registry

- Replace `frontmatter_only` with policy lookup.
- Convert current prose/semantic/frontmatter logic into explicit policies.

Success criterion: adding a new review type no longer requires threading another boolean through the selector.

### Phase 3. Separate diff materialization

- Policy returns decision + diff kind
- renderer or engine builds diffs lazily only when needed

Success criterion: path-only output avoids unnecessary blob diff work.

### Phase 4. Shared review-path / state utilities

- Unify path mapping and review-state loading across selector-adjacent scripts
- add collision-safe review naming before recursive scope is enabled

Success criterion: one canonical mapping used everywhere.

### Phase 5. Add scope / filter / sort features

Only after the above:

- `--recursive`
- `--dir`
- `--status`
- `--tag`
- `--type`
- `--sort`
- `--limit`

At that point these become straightforward feature additions rather than structural stress.

## What to avoid

- Do not add many more review-type-specific booleans.
- Do not make recursive inventory the default before canonical review path mapping exists.
- Do not couple sorting requirements to policy evaluation more than necessary.
- Do not introduce an external config file yet unless there is clear evidence of many selector types or per-installation overrides.
- Do not build a shell-pipeline architecture; the complexity is not justified yet.

## Decision

Reject the "extend the existing script with more flags and no architectural change" approach.

Use a staged refactor:

1. extract selector engine
2. install policy registry
3. unify shared review-state helpers
4. then add scope/filter/sort features

That sequence is slower than adding two flags immediately, but much cheaper than repeatedly patching a script that is clearly becoming shared infrastructure.
