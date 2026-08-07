---
gate_id: semantic/underspecified-assertions
name: Underspecified assertions
description: 'A load-bearing assertion leaves an argument-relevant mechanism, comparison, threshold, scope, timeframe, or consequence unresolved, so materially different readings change its truth, support, or implication.'
type: kb/types/review-gate.md
lens: semantic
watches: [body]
staleness: changed
---

## Failure mode

A load-bearing assertion sounds settled while leaving an argument-relevant choice unresolved. Two or more materially different readings fit the text because it does not identify a needed mechanism, comparison basis, threshold, scope, timeframe, or consequence. Choosing among those readings would change what makes the assertion true, what evidence supports it, or what follows from it.

This is semantic underspecification, not merely a broad claim, an unfamiliar term, or the absence of numerical detail. A broad assertion can be exact. Missing detail matters here only when different values or meanings would change the argument.

## Test

Inspect assertions that do argumentative work: premises, evidence summaries, inference steps, definitions, recommendations, and stated boundaries. Do not require transitions, headings, or purely illustrative remarks to carry the same semantic load.

For each potentially underspecified assertion:

1. State two reasonable readings that are both consistent with the text. Do not use strained grammatical parses or merely synonymous paraphrases.
2. Name the unresolved choice: mechanism, comparison dimension or baseline, threshold, population or scope, timeframe, or operational consequence.
3. Apply the **materiality test**. Ask whether choosing one reading rather than the other changes at least one of:
   - the conditions under which the assertion is true;
   - the evidence needed to support it;
   - the inference, prediction, recommendation, or intervention that follows.
4. Check nearby context. If the paragraph defines the term, identifies the causal route, supplies the comparison, or states the consequence, the assertion passes even if its first clause is compressed or metaphorical.
5. Report WARN only when the assertion is load-bearing, at least two reasonable readings remain, and their difference passes the materiality test. Quote the assertion, give the competing readings, name the unresolved choice, and state what changes between them.

Return PASS when no such assertion remains. A possible ambiguity that the reviewer cannot show to be material may be mentioned as INFO while the final verdict remains PASS. Return ERROR only when the target text is unavailable or cannot be inspected.

This gate reports the unresolved choice; it does not repair it. Do not invent a number, mechanism, threshold, definition, source, or timeframe. Do not recommend generic hedges or defensive qualifiers such as "may", "often", or "in some cases" as substitutes for resolving the choice. The author may later clarify, narrow, support, or remove the assertion.

Do not flag adjacent failures here:

- **Factual error or irrelevance:** a clear assertion may be false or may not support the conclusion. This gate tests whether its meaning is materially unresolved, not whether it is correct or relevant.
- **Unearned generality:** broad or abstract wording belongs to that gate when its scope is clear but unjustifiably wide. Generality alone is not underspecification.
- **Parsing ambiguity:** competing readings caused by modifier attachment, pronoun reference, or negation scope belong to `sentence/parsing-ambiguity`.
- **Explanatory-reach:** a stable claim may lack an adequate explanation. Flag it here only when the wording itself leaves multiple materially different causal claims open.
- **Unsupported precision or grounding:** an exact number, date, mechanism, or scope may lack evidence. Greater specificity is not automatically better.
- **Missing detail without argumentative effect:** do not demand a baseline, date, unit, or threshold when supplying it would not change truth, support, or consequence.

## Example (fail)

> Sprawling supply chains make chip smuggling feasible.

One reading is that more intermediaries create more concealment and transshipment opportunities; another is that fragmented jurisdictions create enforcement gaps. The first calls for evidence about routes and intermediaries and suggests traceability controls. The second calls for evidence about jurisdictional gaps and suggests enforcement coordination. The unresolved causal mechanism changes both support and intervention.

> The shipment contained enough compute to matter.

"Matter" could mean enough compute to fine-tune a model, serve an existing model, or alter national training capacity. Each threshold makes a different claim and requires different evidence. The sentence does not select one.

> Exports fell 30% after the controls, so the controls produced a durable reduction.

If the comparison is one week after introduction, the number does not support the same consequence as a year-over-year comparison sustained for twelve months. Because the inference claims durability, the missing measurement and persistence timeframe is material.

## Example (pass)

> Chips are compact.

This presents one ordinary property. Do not flag it merely because it gives no dimensions. It may be false for the hardware under discussion or irrelevant to the conclusion, but those are different defects unless the argument depends on an unstated size threshold.

> Every rule accepted by this path is loaded before the next revision episode.

The assertion is broad but exact: it identifies the population, condition, action, and time boundary. Breadth is not vagueness.

> The validator rejected the malformed entry.

No date is supplied, but the assertion concerns whether the event occurred. A timeframe is not material to its stated truth or consequence.

> The reseller exemption hollows out the control: prohibited chips can reach the same buyers through exempt subsidiaries, so the control no longer blocks that route.

The evaluative metaphor is immediately resolved into an operational consequence. It does not leave the reader to choose what "hollows out" means.
