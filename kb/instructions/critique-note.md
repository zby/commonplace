---
description: Build the strongest case that a note's central commitment is wrong, then check whether the note already answers it; use when a caller needs a report-only adversarial assay.
type: kb/types/instruction.md
---

# Critique a note

Build the strongest case that a note's central commitment is wrong, then check whether the note already answers it — and report honestly when the strongest available case does not survive. This is an open-ended, report-kind assay: it completes with a critique, not a PASS/WARN/FAIL verdict. `ERROR` reports inability to complete the assay and fails the job; a note that withstands the strongest attack is a completed critique, not an `ERROR`. Write the report; do not touch the note.

Run it in a **fresh sub-agent** (or a different runner than wrote the note) so the critic has no sympathy for the note's framing.

The caller owns reviewer lifecycle. After the report has been written and verified, close, terminate, or release the critic with the harness lifecycle operation. The critic is a single-use context and must not receive follow-up work.

## The critique

Attack the note's central commitment in the mode its artifact kind calls for — steelman the opposing position for a claim, find the counterexample or the idle distinction for a definition, show the wrong outcome for a procedure, find the discrepancy for a description.

Make the attack **maximally strong**: the version an informed opponent would actually make, named to a concrete stance — not a balanced "some might disagree." If the author could dismiss it in one sentence, it is not strong enough yet.

Constructing that attack has two honest outcomes. Usually the strongest objection **lands**, fully or partially, and the report presents it. But sometimes the strongest case an informed opponent could make is one the note already fully answers, or one that does not apply on inspection — that is a first-class result, **no surviving attack**, not a failure to complete. Do **not** escalate to a contrived, vague, or unfalsifiable objection to satisfy the format: an objection the author cannot dismiss *because it is slippery* is weaker, not stronger. "No surviving attack" is earned, not a default — you must still have built the strongest real objection, and you must name it and show exactly why it fails, so the finding is inspectable rather than a fluent "looks fine". Default to attacking hard; conclude no surviving attack only when the strongest objection you can build genuinely does not land. When reaching **no surviving attack** rests on domain knowledge you are not confident you have — a competent specialist might build an objection you could not — report it as **no surviving attack (low confidence — needs domain check)** rather than a clean result, so a reader escalates instead of treating the commitment as settled. This does not remove the limit that one critic cannot certify its own objection is the strongest; it makes that residual visible for the other review lenses and the human to catch.

## Report shape

The caller supplies the output destination and owns any surrounding protocol markers. When run through a review job, write only the caller's `job-output.md`; when run by hand, name a report path explicitly before dispatch. Mutate nothing else.

```markdown
# Critique: <note title>

**Note:** <path>
**Central commitment:** <one sentence>
**Critique mode:** <claim | definition | procedure | description>
**Attack outcome:** <lands | partially lands | no surviving attack | no surviving attack (low confidence — needs domain check)>

## Strongest case against it
<the strongest real objection — who holds it, why, and its best reasoning; state it even when the outcome is "no surviving attack", so the conclusion is inspectable>

## How the note engages it
<engaged | partially engaged | unengaged | fully answers, with where in the note>

## Constructive findings
- <what would let the note contend with the attack; "none — the note already answers the strongest objection" when the outcome is no surviving attack>

## Secondary objections (optional)
- <weaker but real objections worth noting>
```

---

Relevant Notes:

- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) — rests-on: this critique's report-only output and fresh-runner requirement are the decorrelation and no-verdict-authority conditions that note's defense depends on
