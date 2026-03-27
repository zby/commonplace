# Review system

The review system checks KB notes against **gates** — small, focused quality checks. Each gate tests one failure mode (e.g. "anthropomorphic framing," "grounding alignment," "broken link path").

## Concepts

**Gate.** A markdown file in `kb/instructions/review-gates/{lens}/{name}.md` that defines a failure mode and a test. The `{lens}/{name}` path is the gate id (e.g. `prose/source-residue`).

**Bundle.** A directory of gates sharing a lens. `prose` is the bundle of all gates in `kb/instructions/review-gates/prose/`. Bundles are not configuration — they're just directories.

**Review.** A markdown file recording the result of applying one gate to one note under a specific model. Lives at `kb/reports/reviews/{encoded-note}/{encoded-gate}.{encoded-model}.md`.

**Staleness.** A review is stale when the note or gate it covers has been modified more recently than the review file. Determined by comparing filesystem modification times, like `make`.

**Ack.** Touching a review file to bump its mtime, signaling that a change to the note was inspected and found insignificant for that gate. `touch` is the ack operation.

## File layout

```
kb/instructions/review-gates/
  prose/
    source-residue.md
    confidence-miscalibration.md
    ...
  semantic/
    grounding-alignment.md
    ...
  frontmatter/
  structural/
  complexity/

kb/reports/reviews/
  kb__notes__backlinks/
    prose__source-residue.opus-4-6.md
    semantic__grounding-alignment.opus-4-6.md
    ...
```

### Path encoding

- Note path: strip `.md`, replace `/` with `__`. `kb/notes/backlinks.md` → `kb__notes__backlinks`
- Gate id: replace `/` with `__`. `prose/source-residue` → `prose__source-residue`
- Model: replace non-alphanumeric characters with `-`, lowercase. `opus 4.6` → `opus-4-6`
- Full review filename: `{encoded-gate}.{encoded-model}.md`

The model comes from the `COMMONPLACE_REVIEW_MODEL` environment variable. A review from one model does not satisfy staleness checks for a different model.

## Staleness model

Staleness uses filesystem modification times. Three files participate:

1. **Note** — the file being reviewed
2. **Gate** — the gate definition file
3. **Review** — the recorded review file

Rules:

- **Review missing** → stale (reason: `missing-review`)
- **Gate mtime > review mtime** → stale (reason: `gate-changed`). The gate definition changed; the review may no longer apply the right test.
- **Note mtime > review mtime** → stale (reason: `note-changed`). The selector generates a diff of the note since the review's mtime and includes it in the output so a sweep agent can judge significance.

When no rule triggers, the review is **fresh**.

### Ack workflow

A sweep agent sees a stale review, inspects the diff, and decides whether the change matters for that gate. If the change is insignificant (e.g. a typo fix doesn't affect `semantic/grounding-alignment`), the agent runs `touch` on the review file. This bumps the mtime past the note's mtime, making the review fresh again.

If the change is significant, the agent writes a new review body to the file, which also updates the mtime.

### Why mtime

Filesystem modification times give make-like dependency tracking with no bookkeeping:

- No index to maintain or rebuild
- No hash computation
- No finalize step after writing a review
- Ack is just `touch`

Tradeoffs:

- **False staleness** (note mtime bumped by checkout): cheap — the sweep sees an empty diff and touches the review.
- **False freshness** (review mtime bumped by checkout): rare but silent. If `git checkout` rewrites a review file (because it differs between branches), the review's mtime jumps to "now," hiding genuine note changes. This requires the review to differ across branches, which is unusual. If you suspect this after branch operations, re-run the sweep to catch any hidden staleness.

## Scripts

| Script | Purpose |
|---|---|
| `resolve_gates.py` | Resolve gate ids and bundle names to concatenated gate text with output paths |
| `gate_selector.py` | List stale (note, gate) pairs using mtime comparison |
| `warn_selector.py` | List notes with WARN-level findings in their gate reviews |

### resolve_gates.py

```bash
# Individual gates
uv run scripts/resolve_gates.py prose/source-residue semantic/grounding-alignment

# Expand a bundle
uv run scripts/resolve_gates.py prose

# With output paths for a target note
uv run scripts/resolve_gates.py --note kb/notes/backlinks.md prose
```

### gate_selector.py

```bash
# All stale pairs across all gates
uv run scripts/gate_selector.py --all-gates

# Stale pairs for one bundle
uv run scripts/gate_selector.py prose

# Filter to one note
uv run scripts/gate_selector.py --all-gates kb/notes/backlinks.md

# JSON output (includes diff for note-changed pairs)
uv run scripts/gate_selector.py --all-gates --json
```

## Agent workflow

### Running a review bundle on a note

Instruction: `kb/instructions/run-review-bundle-on-note.md`

1. `uv run scripts/resolve_gates.py --note {note} {gates-or-bundles}` — one call, gets all gate text and output paths
2. Read the note
3. Apply each gate, write review body to the printed path
4. Done — mtime marks it current

### Sweep (batch staleness check)

Instruction: `kb/instructions/review-sweep.md`

1. `uv run scripts/gate_selector.py {bundle-or-all} --json` — get stale pairs with diffs
2. Triage by reason: `missing-review` and `gate-changed` need fresh reviews; `note-changed` needs diff inspection
3. For significant changes: load gates via `resolve_gates.py`, write fresh reviews
4. For insignificant changes: `touch` the review file to ack
