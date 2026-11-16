---
gate_id: complexity/framework-decoration
name: Framework decoration
description: 'A table, taxonomy, framework, notation or equation looks rigorous but does not communicate more than a short paragraph would.'
type: types/review-gate.md
lens: complexity
watches: [body]
staleness: changed
depth: 4
---

## Failure mode

A table, taxonomy, framework, piece of notation or equation looks rigorous but does not communicate more than a short paragraph would.

## Test

Ask whether the structure can be deleted and replaced with one sentence without losing meaningful information. Meaningful information includes discriminative categories, boundary cases, decision rules, and inference steps that support the note's stated claim. Do not treat a distinction as meaningful merely because deleting it loses information: identify what inference, decision, prediction, compression, or repeated lookup the distinction enables in the note. WARN when a structure introduces more categories, vocabulary, or cross-references than the argument later uses, even if prose could not preserve every cell verbatim. If the same route and distinctions survive as one sentence, the framework is decorative rather than load-bearing.

For each piece of notation, equation or formal-looking decomposition, apply two further checks. Delete it mentally and re-read the passage: if clarity and precision are unchanged, the formalism is decorative. Ask whether someone could use it to make a quantitative prediction or derive a non-obvious consequence: if not, it is not doing formal work.

Report all instances, not just the first.
