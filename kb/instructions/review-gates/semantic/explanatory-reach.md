---
gate_id: semantic/explanatory-reach
name: Explanatory-reach
description: 'The note records a pattern or outcome without a mechanism that constrains why it holds or what would make it fail.'
type: kb/types/review-gate.md
lens: semantic
watches: [body]
staleness: changed
requires_trait: title-as-claim
---

## Failure mode

The note records a pattern or outcome without explaining why it holds. The claim is easy to vary — you could swap the evidence or change a premise and the conclusion would still sound plausible, because nothing in the argument constrains it.

## Test

For the central claim:

1. Identify the mechanism or explanation the note offers for *why* the claim holds.
2. Try varying one premise the note actually uses. Does the conclusion change? If the same conclusion follows regardless, the explanation is not load-bearing — the note is adaptive (records what works) rather than explanatory (captures why).
3. Check falsifiability: is there any observation or evidence that would contradict the claim? If nothing could, the claim may be unfalsifiable.
4. Check for ad-hoc accommodation: does the note add qualifications or escape hatches that protect the claim from counterexamples without improving the explanation?
5. Do not repair the mechanism while reviewing. Judge the explanation present in the artifact, not a stronger route that would make the same conclusion work.

WARN when the note presents a claim with no mechanism, or the mechanism is easy to vary without breaking the conclusion. INFO when a mechanism is present but thin — plausible but not yet constrained enough to be hard-to-vary.
