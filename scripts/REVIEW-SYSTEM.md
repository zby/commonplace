# Review system

The review system checks KB notes against **gates** — small, focused quality checks. Each gate tests one failure mode (e.g. "anthropomorphic framing," "grounding alignment," "broken link path").

## Concepts

**Gate.** A markdown file in `kb/instructions/review-gates/{lens}/{name}.md` that defines a failure mode and a test. The `{lens}/{name}` path is the gate id (e.g. `prose/source-residue`).

**Bundle.** A directory of gates sharing a lens. `prose` is the bundle of all gates in `kb/instructions/review-gates/prose/`. Bundles are not configuration — they're just directories.

**Review.** A markdown file recording the result of applying one gate to one note under a specific model. Lives at `kb/reports/reviews/{encoded-note}/{encoded-gate}.{encoded-model}.md`.

**Staleness.** A review is stale when the current note content or gate definition no longer matches the acceptance metadata stored inside the review file.

**Ack.** Rewriting the review metadata so `last-accepted-*` points at the current note revision, signaling that a change was inspected and found insignificant for that gate.

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

Staleness uses review metadata stored inside the review file. Three artifacts participate:

1. **Note** — the file being reviewed
2. **Gate** — the gate definition file
3. **Review metadata** — the accepted note revision and gate fingerprint recorded in the review file

Rules:

- **Review missing** → stale (reason: `missing-review`)
- **Metadata missing** → stale (reason: `missing-review`). A body-only review file does not satisfy freshness.
- **Gate fingerprint changed** → stale (reason: `gate-changed`). The gate definition changed; the review may no longer apply the right test.
- **Accepted note sha differs from current note sha** → stale (reason: `note-changed`). The selector generates a diff from the last accepted note revision to the working tree so a sweep agent can judge significance.

When no rule triggers, the review is **fresh**.

### Ack workflow

A sweep agent sees a stale review, inspects the diff, and decides whether the change matters for that gate. If the change is insignificant (e.g. a typo fix doesn't affect `semantic/grounding-alignment`), the agent runs `uv run scripts/ack_gate_review.py {note-path} {gate-id} ...`. This rewrites `last-accepted-*` to the current note revision and keeps the prior `last-full-review-*` fields intact.

If the change is significant, the agent writes a fresh review body with a fresh metadata block.

### Why metadata

Review files may be copied, packaged, or checked out independently of their original filesystem timestamps. Metadata stored inside the artifact survives that distribution path.

Tradeoffs:

- Review writers must emit the metadata block.
- Ack is a metadata rewrite, not a bare `touch`.
- Diffs depend on the accepted blob still being available in git object storage; `scripts/review_prereqs.sh` writes the blob to support this.

## Scripts

| Script | Purpose |
|---|---|
| `resolve_gates.py` | Resolve gate ids and bundle names to concatenated gate text with output paths |
| `gate_selector.py` | List stale (note, gate) pairs using review metadata |
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
3. For each gate, run `scripts/review_prereqs.sh {note} {gate-id}` and paste the emitted metadata block into the review header
4. Apply each gate, write the review body to the printed path
5. Done — the metadata marks it current

### Sweep (batch staleness check)

Instruction: `kb/instructions/review-sweep.md`

1. `uv run scripts/gate_selector.py {bundle-or-all} --json` — get stale pairs with diffs
2. Triage by reason: `missing-review` and `gate-changed` need fresh reviews; `note-changed` needs diff inspection
3. For significant changes: load gates via `resolve_gates.py`, write fresh reviews
4. For insignificant changes: run `uv run scripts/ack_gate_review.py {note-path} {gate-id} ...` to rewrite acceptance metadata
