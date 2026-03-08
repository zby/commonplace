---
description: Catalogue of periodic KB maintenance operations and distillation status, used as a staging ground before promotion into kb/instructions procedures
type: note
traits: [has-implementation]
areas: [kb-design]
status: current
---

# Maintenance operations catalogue should stage distillation into instructions

Periodic operations start as manual procedures. A catalogue keeps them visible, comparable, and editable while they are still being learned. Once an operation is stable enough, it should be distilled into `kb/instructions/` as an execution-oriented procedure.

This note is that staging ground.

## Distillation pipeline

1. Capture the operation here after first useful use.
2. Re-run in varied contexts and tighten ambiguous steps.
3. Mark as ready when inputs, outputs, and decision points are stable.
4. Distill into `kb/instructions/` and link back from this catalogue.

## Catalogue

### Orphan note detection

- Trigger: heartbeat run, user request, or pre-release hygiene pass
- Output: list of notes with no inbound links
- Distillation status: staging

```bash
for f in kb/notes/*.md; do
  fname=$(basename "$f")
  rg -q "$fname" --glob "*.md" kb/notes/ || echo "Orphan: $f"
done
```

### Raw text capture detection

- Trigger: periodic cleanup before curation/connect sweeps
- Output: files without frontmatter that may need promotion from `text` to `note`
- Distillation status: staging

```bash
rg -L "^---" kb/notes/*.md
```

### Neighborhood tension review (target note + linked notes)

- Trigger: after major edits, before promoting status, or on explicit review request
- Input: a target note path
- Output: contradiction/tension/redundancy findings and improvement actions
- Distillation status: staging

Procedure:

1. Read the target note.
2. Enumerate outbound links from the note.
3. Enumerate inbound links to the note (who cites it).
4. Read the neighborhood and flag:
   - Contradictions (claims that cannot both hold as written)
   - Tensions (scope mismatch, unstated assumptions, unresolved caveats)
   - Redundancies (duplicate claims that should merge or cross-link)
   - Improvement opportunities (missing caveats, weak link semantics, stale framing)
5. Apply fixes when clear; otherwise append one-line follow-ups to `kb/log.md`.

Helper commands:

```bash
NOTE="kb/notes/<target>.md"
BASENAME=$(basename "$NOTE")

# Outbound markdown links declared in the target note
rg -o '\]\(([^)]+\.md)\)' "$NOTE" -r '$1' --no-filename | sort -u

# Inbound references to the target note from kb/notes
rg -l "$BASENAME" kb/notes --glob "*.md"
```

---

Relevant Notes:

- [periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing](./periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md) — foundation: routing docs stay slim while periodic operations are externally triggered
- [instructions-are-skills-without-automatic-routing](./instructions-are-skills-without-automatic-routing.md) — target form: mature catalogue entries become reusable instructions
- [deterministic-validation-should-be-a-script](./deterministic-validation-should-be-a-script.md) — escalation path: deterministic operations can move beyond instructions into scripts

Topics:

- [kb-design](./kb-design.md)
