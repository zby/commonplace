---
type: types/type-spec.md
name: review-result
description: "One completed gate, conformance or critique assessment with structured findings and controller-owned execution provenance"
schema: ./review-result.schema.yaml
---

# Review result

A review result records one assessment of captured target text against a criterion. Completion means the output passed deterministic checks, not that its judgment is correct. A report outcome is not a favorable verdict. Use this type for individual gate, type-conformance, collection-conformance and critique results, not for combined improvement packets or connection discovery.

## Content

Findings state what the assessed text establishes or fails to establish. Each passage finding quotes enough verbatim text to identify one contiguous span uniquely. A quote is matched after whitespace and typographic quote marks are normalized, so a line wrap in the target does not break it. A quote therefore identifies a passage and is not a byte-exact copy of it. A consumer that needs the exact span locates the quote in the captured target, which holds the exact bytes. A document-wide or absence finding explains the condition without inventing a quotation. Finding levels belong to verdict criteria; critique reports instead state whether the strongest attack lands and how the note engages it. An empty findings list is an honest completed result when no finding remains.

The body explains the assessment without repeating every structured finding. A critique preserves its central commitment, critique mode, strongest case, the note's response and constructive findings, including why an attack does not survive. Low-confidence no-surviving-attack findings leave the need for a domain check visible.

## Field ownership

The worker fragment supplies only `type`, `findings`, `outcome`, optional `attack-outcome`, and the body. Findings precede the outcome so the serialized verdict follows its rationale. The fragment is not a complete saved artifact. The controller completes and validates it; workers never assert hashes, execution identities or timestamps.

| Fields | Owner and meaning |
|---|---|
| `type`, `findings`, `outcome`, `attack-outcome` | Worker assessment; findings contain `scope`, `quotes`, `reason`, and `level` for verdicts |
| `description`, `format`, `contract` | Controller's result-format identity and expected verdict/report contract |
| `note`, `criterion` | Original target and criterion identities |
| `note-sha256`, `criterion-sha256` | Freshness hashes; the note hash may cover normalized watched parts, not exact bytes |
| `target-sha256`, `target-capture` | Exact assessed UTF-8 bytes and their retained repository-relative location |
| `observation`, `contract-sha256` | Execution observation and captured output-contract identity |
| `profile`, `model`, `run`, `launch`, `completed-at` | Requested execution configuration and observed execution provenance |
| `raw-output`, `raw-output-sha256` | Retained original worker fragment, distinct from this completed artifact |

## Template

Worker fragment for a verdict criterion; code supplies the remaining fields:

```markdown
---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The claim omits the condition needed for its stated conclusion."
    level: warn
outcome: warn
---

# Review

## Summary

The conclusion needs its missing condition.
```

A critique fragment uses `outcome: report`, supplies `attack-outcome`, and omits finding levels. Its body retains the critique instruction's sections. Neither fragment uses a terminal `## Result:` line. Operational production and publication belong to the review command, not to this type.
