---
description: Build the strongest case that a note's central commitment is wrong, then check whether the note already answers it; use when a caller needs a report-only adversarial assay.
type: kb/types/instruction.md
---

# Critique a note

Build the strongest case that a note's central commitment is wrong, then check whether the note already answers it. This is a report-kind assay: it completes with a critique, not a PASS/WARN/FAIL/ERROR verdict. Write the report; do not touch the note.

Run it in a **fresh sub-agent** (or a different runner than wrote the note) so the critic has no sympathy for the note's framing.

## The critique

Attack the note's central commitment in the mode its register calls for — steelman the opposing position for a claim, find the counterexample or the idle distinction for a definition, show the wrong outcome for a procedure, find the discrepancy for a description.

Make the attack **maximally strong**: the version an informed opponent would actually make, named to a concrete stance — not a balanced "some might disagree." If the author could dismiss it in one sentence, it is not strong enough yet.

## Report shape

The caller supplies the output destination and owns any surrounding protocol markers. When run through a review job, write only the caller's `bundle-output.md`; when run by hand, name a report path explicitly before dispatch. Mutate nothing else.

```markdown
# Critique: <note title>

**Note:** <path>
**Central commitment:** <one sentence>
**Critique mode:** <claim | definition | procedure | description>

## Strongest case against it
<who holds it, why, and its best reasoning>

## How the note engages it
<engaged | partially engaged | unengaged, with where in the note>

## Constructive findings
- <what would let the note contend with the attack>

## Secondary objections (optional)
- <weaker but real objections worth noting>
```

---

Relevant Notes:

- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) — rationale: this critique's report-only output and fresh-runner requirement are the decorrelation and no-verdict-authority conditions that note's defense depends on
