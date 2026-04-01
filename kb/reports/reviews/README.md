# Reviews

Automated quality reviews of `kb/notes/`. Each review applies one gate (a focused quality check) to one note. Staleness is tracked by metadata stored inside the review file.

**System design:** [scripts/REVIEW-SYSTEM.md](../../../scripts/REVIEW-SYSTEM.md)

## Bundles

- **accessibility** — gates in `kb/instructions/review-gates/accessibility/`
- **complexity** — gates in `kb/instructions/review-gates/complexity/`
- **frontmatter** — gates in `kb/instructions/review-gates/frontmatter/`
- **prose** — gates in `kb/instructions/review-gates/prose/`
- **semantic** — gates in `kb/instructions/review-gates/semantic/`
- **sentence** — gates in `kb/instructions/review-gates/sentence/`
- **structural** — gates in `kb/instructions/review-gates/structural/`

## File naming

Reviews: `{encoded-note-path}/{encoded-gate-id}.{encoded-model}.md`

- Note path: strip `.md`, replace `/` with `__`
- Gate id: replace `/` with `__`
- Model: non-alphanumeric → `-`, lowercase

Example: reviewing `kb/notes/backlinks.md` against `prose/source-residue` with model `opus 4.6` → `kb__notes__backlinks/prose__source-residue.opus-4-6.md`

## Instructions

- **Review one note:** `kb/instructions/run-review-bundle-on-note.md` — explicit note + gates
- **Batch sweep:** `kb/instructions/review-sweep.md` — run selector, triage by reason, review or ack

## Running

```bash
# Resolve gates
uv run scripts/resolve_gates.py prose

# List all stale (note, gate) pairs
uv run scripts/gate_selector.py --all-gates

# List stale pairs for one bundle
uv run scripts/gate_selector.py prose

# JSON output with diffs
uv run scripts/gate_selector.py --all-gates --json

# Ack a review (note change was insignificant for this gate)
uv run scripts/ack_gate_review.py kb/notes/backlinks.md prose/source-residue
```

## Re-running

Writing a new review body overwrites the file and refreshes its acceptance metadata, marking it current. Commit before re-running if you want historical snapshots.
